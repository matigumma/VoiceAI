#!/usr/bin/env python3

import sys
import os
from pathlib import Path
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")

def main():
    # Read piped input
    input_text = sys.stdin.read().strip()

    if not input_text:
        print("No input received from the console.")
        return

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Generate speech using OpenAI API
    speech_file_path = Path("/tmp") / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=input_text
    )

    response.stream_to_file(speech_file_path)

    # Optionally, play the audio file using a system call (Mac-specific example)
    os.system(f"afplay {speech_file_path}")

if __name__ == "__main__":
    main()
