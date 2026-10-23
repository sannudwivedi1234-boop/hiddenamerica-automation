import random
import asyncio
from pathlib import Path
import edge_tts

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

USA_FACTS = [
    {
        "title": "Why Is Alaska So Huge?",
        "script": (
            "Did you know Alaska is larger than Texas, "
            "California, and Montana combined? "
            "It became part of the United States in 1867. "
            "Follow Hidden America 2030 for more amazing facts!"
        )
    },
    {
        "title": "America's Biggest State",
        "script": (
            "Alaska is the largest US state by land area. "
            "It is famous for glaciers, mountains, and wildlife. "
            "Would you visit Alaska? Tell us in the comments!"
        )
    }
]

async def create_voice(text, output_path):
    voice = edge_tts.Communicate(
        text,
        voice="en-US-GuyNeural"
    )
    await voice.save(str(output_path))

def generate_script():
    fact = random.choice(USA_FACTS)

    print("TITLE:", fact["title"])
    print("SCRIPT:", fact["script"])

    audio_path = OUTPUT_DIR / "voiceover.mp3"
    asyncio.run(create_voice(fact["script"], audio_path))

    print("VOICEOVER SAVED:", audio_path)

    return fact

if __name__ == "__main__":
    generate_script()
