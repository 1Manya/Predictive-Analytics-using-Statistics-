"""
Assignment - Mashup
Program 2: Flask Web App
Roll Number: 102317119
"""

import os
import sys
import re
import zipfile
import smtplib
import threading
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#  CONFIG: Set your Gmail credentials as environment variables 
SENDER_EMAIL    = os.environ.get("SENDER_EMAIL", "")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD", "")


#  Helper: validate email format 
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None


# Helper: run the mashup pipeline 
def run_mashup(singer, num_videos, duration, output_mp3, job_dir):
    """
    Calls the same logic as Program 1 but inside the web app process.
    Returns path to the output mp3 on success, raises Exception on failure.
    """
    os.makedirs(job_dir, exist_ok=True)

    # Use subprocess to call Program 1 script
    result = subprocess.run(
        [sys.executable, "102317119.py", singer, str(num_videos), str(duration), output_mp3],
        capture_output=True, text=True, cwd=os.path.dirname(os.path.abspath(__file__))
    )

    if result.returncode != 0:
        raise Exception(result.stderr or result.stdout)

    return output_mp3


#  Helper: zip the output file 
def zip_file(mp3_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(mp3_path, os.path.basename(mp3_path))


#  Helper: send email with zip attachment 
def send_email(to_email, zip_path, singer):
    msg = MIMEMultipart()
    msg['From']    = SENDER_EMAIL
    msg['To']      = to_email
    msg['Subject'] = f"Your Mashup is Ready! 🎵 - {singer}"

    body = f"""Hi there!

Your Mashup for "{singer}" has been successfully created! 🎶

Please find the attached ZIP file containing your mashup MP3.

Enjoy your music!

— Mashup Creator (Roll No: 102317119)
"""
    msg.attach(MIMEText(body, 'plain'))

    # Attach the zip file
    with open(zip_path, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(zip_path)}"')
        msg.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

def process_mashup(singer, num_videos, duration, email):
    import time
    import traceback
    job_id  = str(int(time.time()))
    job_dir = os.path.join("jobs", job_id)
    os.makedirs(job_dir, exist_ok=True)

    output_mp3 = os.path.join(job_dir, f"mashup_{job_id}.mp3")
    output_zip = os.path.join(job_dir, f"mashup_{job_id}.zip")

    try:
        print(f"[INFO] Starting mashup for {singer}, {num_videos} videos, {duration}s", flush=True)
        run_mashup(singer, num_videos, duration, output_mp3, job_dir)
        print(f"[INFO] Mashup done, zipping...", flush=True)
        zip_file(output_mp3, output_zip)
        print(f"[INFO] Sending email to {email}...", flush=True)
        send_email(email, output_zip, singer)
        print(f"[DONE] Email sent to {email}", flush=True)
    except Exception as e:
        print(f"[ERROR] Job {job_id} failed:", flush=True)
        print(traceback.format_exc(), flush=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    singer     = request.form.get("singer", "").strip()
    num_videos = request.form.get("num_videos", "").strip()
    duration   = request.form.get("duration", "").strip()
    email      = request.form.get("email", "").strip()

    errors = []

    if not singer:
        errors.append("Singer name is required.")

    try:
        num_videos = int(num_videos)
        if num_videos <= 10:
            errors.append("Number of videos must be greater than 10.")
    except ValueError:
        errors.append("Number of videos must be a valid number.")
        num_videos = None

    try:
        duration = int(duration)
        if duration <= 20:
            errors.append("Duration must be greater than 20 seconds.")
    except ValueError:
        errors.append("Duration must be a valid number.")
        duration = None

    if not is_valid_email(email):
        errors.append("Please enter a valid email address.")

    if errors:
        return jsonify({"status": "error", "errors": errors}), 400

    # Start background thread so the web request doesn't block
    t = threading.Thread(target=process_mashup, args=(singer, num_videos, duration, email))
    t.daemon = True
    t.start()

    return jsonify({
        "status": "success",
        "message": f"Your mashup for '{singer}' is being created! You'll receive an email at {email} shortly."
    })
@app.route("/test")
def test():
    import traceback
    results = {}
    
    # Test 1: ffmpeg
    try:
        import subprocess
        r = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        results["ffmpeg"] = "OK - " + r.stdout.split('\n')[0]
    except Exception as e:
        results["ffmpeg"] = f"FAILED - {str(e)}"
    
    # Test 2: yt-dlp
    try:
        import yt_dlp
        results["yt_dlp"] = "OK"
    except Exception as e:
        results["yt_dlp"] = f"FAILED - {str(e)}"

    # Test 3: email
    try:
        import smtplib
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
        results["email"] = "OK - Login successful"
    except Exception as e:
        results["email"] = f"FAILED - {str(e)}"

    # Test 4: env variables
    results["SENDER_EMAIL"] = SENDER_EMAIL if SENDER_EMAIL else "NOT SET"
    results["SENDER_PASSWORD"] = "SET" if SENDER_PASSWORD else "NOT SET"

    return jsonify(results)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
