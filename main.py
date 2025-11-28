from moviepy.editor import *
import os

# Make sure output folder exists
os.makedirs("output", exist_ok=True)

def apply_transformations(video_path, audio_path=None, text=None):
    print("Loading video...")
    video = VideoFileClip(video_path)

    # 1. Resize (50%)
    print("Applying resize...")
    video = video.resize(0.5)

    # 2. Rotate (90 degrees)
    print("Rotating video...")
    video = video.rotate(90)

    # 3. Speed Change (1.5x faster)
    print("Changing speed...")
    video = video.fx(vfx.speedx, 1.5)

    # 4. Black & White Filter
    print("Applying color filter...")
    video = video.fx(vfx.blackwhite)

    # 5. Add Text
    if text:
        print("Adding text...")
        txt = TextClip(text, fontsize=60, color='white')
        txt = txt.set_position(("center", "bottom")).set_duration(video.duration)
        video = CompositeVideoClip([video, txt])

    # 6. Replace background audio (optional)
    if audio_path:
        print("Replacing audio...")
        new_audio = AudioFileClip(audio_path)
        video = video.set_audio(new_audio)

    # FINAL SAVE
    output_path = "output/transformed_video.mp4"
    print("Saving final video...")
    video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    print("\n✔ DONE — Video saved to:", output_path)


def merge_videos(video_list):
    print("Merging videos...")
    clips = [VideoFileClip(v) for v in video_list]
    final = concatenate_videoclips(clips)
    output_path = "output/merged_video.mp4"
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")
    print("✔ Merged video saved:", output_path)


if __name__ == "__main__":
    # Main transformer
    apply_transformations(
        video_path="input/input_video.mp4",
        audio_path="audios/music.mp3",   # optional
        text="TRANSFORMED VIDEO"         # optional
    )

    # Example: merging videos
    # merge_videos(["videos/part1.mp4", "videos/part2.mp4"])

