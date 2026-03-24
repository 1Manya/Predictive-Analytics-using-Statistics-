# Mashup Creator — Web Application
**Roll Number:** 102317119  
---

## What is this project?

This project is a web-based Mashup Creator that lets you download songs of any singer from YouTube, cut the first few seconds from each, and merge them all into one single MP3 file. The final mashup is sent directly to your email as a ZIP file.

I built this as part of my assignment which required using Python libraries from PyPI to automate the entire process — downloading, converting, cutting, and merging audio files.

---

## How it works

1. You enter a singer name, number of videos, clip duration, and your email
2. The app searches YouTube and downloads N videos of that singer
3. Each video is converted from video format to audio (MP3)
4. The first Y seconds are cut from each audio clip
5. All clips are merged into one final mashup MP3
6. The mashup is zipped and sent to your email automatically

---

## Screenshots

### Web Interface
*(<img width="994" height="1458" alt="image" src="https://github.com/user-attachments/assets/cab09188-5a3c-4da7-970f-2a4577ea645e" />
)*

### Email Received with Mashup
*(<img width="956" height="765" alt="image" src="https://github.com/user-attachments/assets/7cef903c-e245-4c5c-9965-c5dab5ae7cb6" />
)*

---

## Libraries Used

| Library | Purpose | PyPI Link |
|---------|---------|-----------|
| `yt-dlp` | Download YouTube videos | [pypi.org/project/yt-dlp](https://pypi.org/project/yt-dlp) |
| `moviepy` | Convert video to audio | [pypi.org/project/moviepy](https://pypi.org/project/moviepy) |
| `pydub` | Cut and merge audio files | [pypi.org/project/pydub](https://pypi.org/project/pydub) |
| `flask` | Web framework | [pypi.org/project/flask](https://pypi.org/project/flask) |
| `smtplib` | Send email with attachment | Built-in Python library |

---

## Project Structure

```
mashup-102317119/
├── 102317119.py          # Program 1 - Command line tool
├── app.py                # Program 2 - Flask web application
├── requirements.txt      # All required libraries
├── templates/
│   └── index.html        # Frontend web page
└── README.md             # This file
```

---

## Program 1 — Command Line Tool

### Install dependencies
```bash
pip install yt-dlp moviepy pydub
```

### How to run
```bash
python 102317119.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>
```

### Example
```bash
python 102317119.py "Sharry Maan" 20 20 102317119-output.mp3
```

### Input Rules
- Singer name — any valid singer name
- Number of videos — must be greater than 10
- Audio duration — must be greater than 20 seconds
- Output file — must end with .mp3

---

## Program 2 — Flask Web Application

### Live Demo
🔗 *(Add your Render deployed link here)*

### Run locally
```bash
pip install -r requirements.txt
python app.py
```
Then open: **http://localhost:5000**

---

## How to set up Gmail for sending emails

This project uses Gmail to send the mashup file. To run it locally:

1. Enable 2-Step Verification on your Google account
2. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Generate an App Password
4. Set your credentials:

```bash
set SENDER_EMAIL=youremail@gmail.com
set SENDER_PASSWORD=your16charapppassword
```

---

## Deployment

This project is deployed on **Render** (free tier).  
🔗 Live Link: *(Add your link here)*
