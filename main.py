import os
from moviepy.editor import *
from pydub import AudioSegment
import cv2

INPUT = "input/"
OUTPUT = "output/"
VIDEOS = "videos/"
AUDIOS = "audios/"

def ensure_dirs():
    for d in [INPUT, OUTPUT, VIDEOS, AUDIOS]:
        if not os.path.exists(d):
            os.makedirs(d)

def transform_video(video_file):
    video_path = os.path.join(INPUT, video_file)
    output_path = os.path.join(OUTPUT, "transformed_" + video_file)

    clip = VideoFileClip(video_path)
    final = clip.fx(vfx.blackwhite).fx(vfx.speedx, 1.2)
    final.write_videofile(output_path)

    print("✔ Video Transformed:", output_path)

def extract_audio(video_file):
    video_path = os.path.join(INPUT, video_file)
    output_audio = os.path.join(AUDIOS, video_file.replace(".mp4", ".mp3"))

    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(output_audio)

    print("✔ Audio Extracted:", output_audio)

def extract_frames(video_file):
    video_path = os.path.join(INPUT, video_file)
    frame_folder = os.path.join(VIDEOS, video_file.replace(".mp4", ""))

    if not os.path.exists(frame_folder):
        os.makedirs(frame_folder)

    vid = cv2.VideoCapture(video_path)
    count = 0

    while True:
        success, frame = vid.read()
        if not success:
            break
        cv2.imwrite(f"{frame_folder}/frame_{count}.jpg", frame)
        count += 1

    print("✔ Frames Extracted:", frame_folder)

if __name__ == "__main__":
    ensure_dirs()
    files = os.listdir(INPUT)

    for f in files:
        if f.endswith(".mp4"):
            print("Processing:", f)
            transform_video(f)
            extract_audio(f)
            extract_frames(f)

    print("\n🎉 All Done!")
  
