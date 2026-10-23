from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from moviepy import AudioFileClip, ImageClip, concatenate_videoclips

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def create_video(image_path, audio_path, output_path):
    audio = AudioFileClip(str(audio_path))
    original = Image.open(image_path).convert("RGB")

    width, height = 1080, 1920
    scenes = [
        "DID YOU KNOW?",
        "HIDDEN AMERICA",
        "AMAZING USA FACTS",
        "THE SURPRISING TRUTH",
        "FOLLOW FOR MORE"
    ]

    clips = []
    duration = audio.duration / len(scenes)

    try:
        for i, title in enumerate(scenes):
            img = original.copy()

            # Create different visual crops
            scale = 1.0 + (i * 0.08)
            new_w = int(width * scale)
            new_h = int(height * scale)
            img = img.resize((new_w, new_h))

            left = max(0, (new_w - width) // 2)
            top = max(0, (new_h - height) // 2)
            img = img.crop((left, top, left + width, top + height))

            draw = ImageDraw.Draw(img)

            try:
                font = ImageFont.truetype(
                    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                    76
                )
            except OSError:
                font = ImageFont.load_default()

            bbox = draw.textbbox((0, 0), title, font=font)
            text_w = bbox[2] - bbox[0]
            x = (width - text_w) // 2
            y = int(height * 0.72)

            draw.rounded_rectangle(
                (40, y - 35, width - 40, y + 130),
                radius=25,
                fill=(10, 25, 45)
            )

            draw.text(
                (x, y),
                title,
                font=font,
                fill="white"
            )

            scene_path = OUTPUT_DIR / f"scene_{i}.jpg"
            img.save(scene_path, quality=90)

            clip = ImageClip(str(scene_path)).with_duration(duration)
            clips.append(clip)

        video = concatenate_videoclips(clips, method="compose")
        video = video.with_audio(audio)

        video.write_videofile(
            str(output_path),
            fps=24,
            codec="libx264",
            audio_codec="aac"
        )

        video.close()

    finally:
        audio.close()
        for clip in clips:
            clip.close()

if __name__ == "__main__":
    print("Hidden America 2030 Video Generator Ready")
