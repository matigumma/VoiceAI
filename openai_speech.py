#!/usr/bin/env python3

import os
from pathlib import Path
from colorama import Fore, Style
from openai import OpenAI
from datetime import datetime

api_key = os.environ.get("OPENAI_API_KEY")

def openai_speech(input_text: str):
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Generate speech using OpenAI API

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    speech_file_path = Path("/tmp") / f"speech_{timestamp}.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=input_text
    )

    response.stream_to_file(speech_file_path)

    print(f"Using {Fore.BLUE}openai_speech{Style.RESET_ALL} function")
    
    return speech_file_path