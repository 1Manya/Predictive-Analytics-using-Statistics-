import os
import re
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request
from topsis_manya_102317119.topsis import topsis

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    file = request.files["file"]
    weights = request.form["weights"]
    impacts = request.form["impacts"]
    email = request.form["email"]

    # -------- VALIDATION -------- #

    weights_list = weights.split(",")
    impacts_list = impacts.split(",")

    if len(weights_list) != len(impacts_list):
        return "Error: Number of weights and impacts must be equal."

    for impact in impacts_list:
        if impact not in ["+", "-"]:
            return "Error: Impacts must be '+' or '-' only."

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Error: Invalid email format."

    # -------- SAVE FILE -------- #

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    output_path = os.path.join(app.config["UPLOAD_FOLDER"], "result.csv")

    # -------- RUN TOPSIS -------- #
    print("Columns in matrix:", len(weights.split(",")))
    import pandas as pd
    df = pd.read_csv(filepath)
    print("Actual criteria columns:", df.shape[1] - 1)

    try:
        topsis(filepath, weights, impacts, output_path)
    except Exception as e:
        return f"Error while processing TOPSIS: {str(e)}"

    # -------- SEND EMAIL -------- #

    try:
        send_email(email, output_path)
    except Exception as e:
        return f"Error sending email: {str(e)}"

    return "Result sent successfully to your email!"



def send_email(receiver_email, file_path):

    sender_email = "yashmiki01@gmail.com"
    app_password = "wlruhglwkfhyedqc"

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "TOPSIS Result"

    msg.set_content("Please find the TOPSIS result attached.")

    # Attach CSV file
    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(file_path)

    msg.add_attachment(file_data,
                       maintype="application",
                       subtype="octet-stream",
                       filename=file_name)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print("Email error:", e)
    print("Sending to:", receiver_email)


if __name__ == "__main__":
    app.run(debug=True)
