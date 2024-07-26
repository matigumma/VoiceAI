#!/usr/bin/env python3

import os
import sys
from openai_speech import openai_speech
from unreal_speech import unreal_speech
from colorama import Fore, Style

def main():
    # Read piped input
    input_text = sys.stdin.read().strip()

    if not input_text:
        print("No input received from the console.")
        return

    speech_file_path = None

    try:
        # Try using the unreal_speech function
        print("Using unreal_speech function")
        speech_file_path = unreal_speech(input_text)
    except Exception as e:
        print("unreal_speech failed with error:")
        print(f"{Fore.RED}{e}{Style.RESET_ALL}")  # Colorized error message
        # Fallback to openai_speech function
        # speech_file_path = openai_speech(input_text)

    if speech_file_path:
        # Optionally, play the audio file using a system call (Mac-specific example)
        os.system(f"afplay {speech_file_path}")

if __name__ == "__main__":
    main()
