import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
"""
Assignment - Mashup

Usage:
    python 102317119.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>

Example:
    python 102317119.py "Sharry Maan" 20 20 102317119-output.mp3
"""

import sys
import os
import subprocess

#  Library availability check 
def check_and_install(package, import_name=None):
    import_name = import_name or package
    try:
        __import__(import_name)
    except ImportError:
        print(f"[INFO] Installing {package} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])


def install_dependencies():
    check_and_install("yt-dlp", "yt_dlp")
    check_and_install("moviepy")
    check_and_install("pydub")


#  Input Validation 
def validate_inputs(singer_name, num_videos_str, duration_str, output_file):
   
    errors = []

    # Validate singer name
    if not singer_name or singer_name.strip() == "":
        errors.append("Singer name cannot be empty.")

    # Validate number of videos
    try:
        num_videos = int(num_videos_str)
        if num_videos <= 10:
            errors.append(f"Number of videos must be greater than 10. You entered: {num_videos}")
    except ValueError:
        num_videos = None
        errors.append(f"Number of videos must be a valid integer. You entered: '{num_videos_str}'")

    # Validate audio duration
    try:
        duration = int(duration_str)
        if duration <= 20:
            errors.append(f"Audio duration must be greater than 20 seconds. You entered: {duration}")
    except ValueError:
        duration = None
        errors.append(f"Audio duration must be a valid integer. You entered: '{duration_str}'")

    # Validate output filename
    if not output_file.endswith(".mp3"):
        errors.append(f"Output file must have .mp3 extension. You entered: '{output_file}'")

    if errors:
        print("\n[ERROR] Invalid inputs detected:")
        for e in errors:
            print(f"  ✗ {e}")
        print("\nUsage: python 102317119.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        print('Example: python 102317119.py "Sharry Maan" 20 20 102317119-output.mp3')
        sys.exit(1)

    return num_videos, duration


#  Step 1: Download Videos from YouTube 
def download_videos(singer_name, num_videos, download_dir="downloads"):
   
    import yt_dlp

    os.makedirs(download_dir, exist_ok=True)

    search_query = f"ytsearch{num_videos}:{singer_name} songs"

    ydl_opts = {
        "format": "mp4/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": os.path.join(download_dir, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": False,
        "no_warnings": True,
        "ignoreerrors": True,         
        "extract_flat": False,
    }

    print(f"\n[STEP 1] Searching and downloading {num_videos} videos for '{singer_name}' ...")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([search_query])
    except Exception as e:
        print(f"[ERROR] Download failed: {e}")
        sys.exit(1)

    # Collect downloaded video files
    video_files = [
        os.path.join(download_dir, f)
        for f in os.listdir(download_dir)
        if f.endswith((".mp4", ".webm", ".mkv"))
    ]

    if not video_files:
        print("[ERROR] No videos were downloaded. Check your internet connection or singer name.")
        sys.exit(1)

    print(f"[✓] Downloaded {len(video_files)} video(s).\n")
    return video_files


#  Step 2: Convert Videos to Audio 
def convert_to_audio(video_files, audio_dir="audios"):
   
    try:
        from moviepy.editor import VideoFileClip  # moviepy v1.x
    except ImportError:
        from moviepy import VideoFileClip          # moviepy v2.x

    os.makedirs(audio_dir, exist_ok=True)
    audio_files = []

    print(f"[STEP 2] Converting {len(video_files)} video(s) to audio ...")

    for idx, video_path in enumerate(video_files, start=1):
        try:
            base_name = os.path.splitext(os.path.basename(video_path))[0]
            audio_path = os.path.join(audio_dir, f"{base_name}.mp3")

            print(f"  [{idx}/{len(video_files)}] Converting: {os.path.basename(video_path)}")

            clip = VideoFileClip(video_path)
            clip.audio.write_audiofile(audio_path, logger=None)
            clip.close()

            audio_files.append(audio_path)

        except Exception as e:
            print(f"  [WARN] Could not convert '{video_path}': {e}. Skipping.")

    if not audio_files:
        print("[ERROR] No audio files were created. Exiting.")
        sys.exit(1)

    print(f"[✓] Converted {len(audio_files)} audio file(s).\n")
    return audio_files


#  Step 3: Cut first Y seconds from each audio 
def cut_audios(audio_files, duration_sec, cut_dir="cut_audios"):
    
    import subprocess
    os.makedirs(cut_dir, exist_ok=True)
    cut_files = []

    duration_ms = duration_sec * 1000  

    print(f"[STEP 3] Cutting first {duration_sec} seconds from each audio ...")

    for idx, audio_path in enumerate(audio_files, start=1):
        try:
            base_name = os.path.basename(audio_path)
            cut_path = os.path.join(cut_dir, base_name)

            print(f"  [{idx}/{len(audio_files)}] Cutting: {base_name}")

            subprocess.run([
            "ffmpeg", "-y", "-i", audio_path,
            "-t", str(duration_sec),
            "-acodec", "libmp3lame", cut_path
            ], capture_output=True)
            cut_files.append(cut_path)

        except Exception as e:
            print(f"  [WARN] Could not cut '{audio_path}': {e}. Skipping.")

    if not cut_files:
        print("[ERROR] No audio files were cut successfully. Exiting.")
        sys.exit(1)

    print(f"[✓] Cut {len(cut_files)} audio file(s).\n")
    return cut_files


#  Step 4: Merge All Audios into One Output File 
def merge_audios(cut_files, output_file):
    """
    Merges all trimmed audio files into a single MP3 output file using pydub.
    """
    # NEW - write a file list and merge with ffmpeg
    list_file = "filelist.txt"
    with open(list_file, "w",encoding="utf-8") as f:
        for cut_path in cut_files:
            f.write(f"file '{os.path.abspath(cut_path)}'\n")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", list_file, "-acodec", "libmp3lame", output_file
    ], capture_output=True, encoding="utf-8")
    print(f"\n[✓] Mashup complete! Output saved as: {output_file}")


#  Main Entry Point 
def main():
    # Check correct number of arguments
    if len(sys.argv) != 5:
        print("\n[ERROR] Incorrect number of arguments.")
        print("Usage: python 102317119.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        print('Example: python 102317119.py "Sharry Maan" 20 20 102317119-output.mp3')
        sys.exit(1)

    singer_name    = sys.argv[1]
    num_videos_str = sys.argv[2]
    duration_str   = sys.argv[3]
    output_file    = sys.argv[4]

    # Validate inputs
    num_videos, duration = validate_inputs(singer_name, num_videos_str, duration_str, output_file)

    print("\n" + "="*60)
    print("        MASHUP CREATOR - 102317119")
    print("="*60)
    print(f"  Singer       : {singer_name}")
    print(f"  # of Videos  : {num_videos}")
    print(f"  Cut Duration : {duration} seconds each")
    print(f"  Output File  : {output_file}")
    print("="*60 + "\n")

    # Install required libraries if missing
    install_dependencies()

    # Run the 4 steps
    video_files = download_videos(singer_name, num_videos)
    audio_files = convert_to_audio(video_files)
    cut_files   = cut_audios(audio_files, duration)
    merge_audios(cut_files, output_file)

    print("\n Done! Y mashup is ready.")


if __name__ == "__main__":
    main()