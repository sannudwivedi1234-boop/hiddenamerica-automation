from pathlib import Path
from moviepy.editor import AudioFileClip, ImageClip

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def create_video(image_path, audio_path, output_path):
    with AudioFileClip(str(audio_path)) as audio:
        video = (
            ImageClip(str(image_path))
            .set_duration(audio.duration)
            .set_audio(audio)
        )

        video.write_videofile(
            str(output_path),
            fps=30,
            codec="libx264",
            audio_codec="aac"
        )

if __name__ == "__main__":
    print("Hidden America 2030 Video Generator")
    print("Video generator is ready.")
