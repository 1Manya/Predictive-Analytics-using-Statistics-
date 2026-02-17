# 🎯 TOPSIS Web Service

A Flask-based web application that performs TOPSIS  a multi-criteria decision-making method and delivers results directly to the user's email.

---

## 📌 What is TOPSIS?

TOPSIS is a decision-making algorithm used to rank alternatives based on multiple criteria. It identifies the best option by finding the alternative closest to the ideal solution and farthest from the negative-ideal solution.

---

## 🚀 Features

- Upload a CSV file with decision matrix data
- Input custom weights and impact directions (`+` / `-`) per criterion
- Validates all user inputs before processing
- Runs TOPSIS algorithm using a custom Python package
- Sends the ranked result CSV directly to the user's email

---

## 🗂️ Project Structure

```
topsis_web_app/
│
├── app.py                  # Main Flask application
├── uploads/                # Temporary storage for uploaded and result files
├── templates/
│   └── index.html          # Frontend UI
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/topsis-web-app.git
cd topsis-web-app
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# OR
source venv/bin/activate     # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Email Credentials

In `app.py`, update the sender email and Gmail App Password:

```python
sender_email = "your_email@gmail.com"
app_password = "your_16_char_app_password"
```
### 5. Run the Application

```bash
python app.py
```

Open your browser and visit: `http://127.0.0.1:5000`

---

## 📋 Input Format

### CSV File

The input file must be a CSV where:
- The **first column** is the name/identifier of each alternative
- The **remaining columns** are numeric criteria values

### Weights

Comma-separated numeric values, one per criterion column.

```
1,1,1,1,1
```

### Impacts

Comma-separated `+` or `-` symbols, one per criterion column.

- `+` → Higher value is better (benefit criterion)
- `-` → Lower value is better (cost criterion)

```
+,+,-,+,+
```

---

## ✅ Input Validations

| Validation | Rule |
|---|---|
| Weights & Impacts count | Must be equal to each other and to the number of criteria columns |
| Impact values | Must be only `+` or `-` |
| Separator | Weights and impacts must be comma-separated |
| Email format | Must follow standard format (e.g., `user@domain.com`) |
| File format | Must be a valid `.csv` file |

---

## 📤 Output

The result CSV is emailed as an attachment to the provided email address. It contains all original data plus two new columns:

- **Topsis Score** — a value between 0 and 1 (higher is better)
- **Rank** — ranking of alternatives from best to worst

---

## 🐍 TOPSIS Package

This project uses a custom Python package:

```
topsis-manya-102317119
```

Install it via pip:

```bash
pip install topsis-manya-102317119
```

---

## 📦 Requirements

```
Flask
pandas
topsis-manya-102317119
```

Generate `requirements.txt` using:

```bash
pip freeze > requirements.txt
```

---

## 📸 Screenshots

### Web Interface

> Form accepts file upload, weights, impacts, and email ID.

![TOPSIS Web Form](![Screenshot_17-2-2026_232417_127 0 0 1](https://github.com/user-attachments/assets/05069ef9-9465-412b-9845-ba7dec9a6185))


---

## 👤 Author

**Manya**  
Roll No: `102317119`  
B.Tech | Thapar Institute of Engineering & Technology  

---

## 📄 License

This project is submitted as part of an academic assignment. All rights reserved.
