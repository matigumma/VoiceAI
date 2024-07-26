import os
from pathlib import Path
from colorama import Fore, Style
import requests
from datetime import datetime
import time

def unreal_speech(text: str):
    auth_token = os.getenv('UNREAL_SPEECH_API_TOKEN')

    response = None

    if len(text) <= 1000:
        response = requests.post(
            'https://api.v7.unrealspeech.com/stream',
            headers = {
                'Authorization' : f'Bearer {auth_token}'
            },
            json = {
                'Text': text, # Up to 1000 characters
                'VoiceId': 'Scarlett', # Dan, Will, Scarlett, Liv, Amy
                'Bitrate': '64k', # 320k, 256k, 192k, ...
                'Speed': '0', # -1.0 to 1.0
                'Pitch': '1', # -0.5 to 1.5
                'Codec': 'libmp3lame', # libmp3lame or pcm_mulaw
            }
        )

        if response.status_code != 200:
            raise Exception(response.text)
        print(f"Using {Fore.GREEN}STREAM unreal_speech{Style.RESET_ALL} function")
    else: 
        if len(text) <= 3000:
            response = requests.post(
                'https://api.v7.unrealspeech.com/speech',
                headers = {
                    'Authorization' : f'Bearer {auth_token}'
                },
                json = {
                    'Text': text, # Up to 1000 characters
                    'VoiceId': 'Scarlett', # Dan, Will, Scarlett, Liv, Amy
                    'Bitrate': '64k', # 320k, 256k, 192k, ...
                    'Speed': '0', # -1.0 to 1.0
                    'Pitch': '1', # -0.5 to 1.5
                    "TimestampType": "sentence"
                }
            )

            if response.status_code != 200:
                raise Exception(response.text)
            
            print(f"Using {Fore.GREEN}SPEECH unreal_speech{Style.RESET_ALL} function")

            task_id = response.json().get('TaskId')
            task_status = response.json().get('TaskStatus')

            # Calculate sleep time based on text length
            sleep_time = len(text) / 700  # 1 second per 700 characters

            while task_status != 'completed':
                time.sleep(sleep_time) 
                status_response = requests.get(
                    f'https://api.v7.unrealspeech.com/speech/{task_id}',
                    headers = {
                        'Authorization' : f'Bearer {auth_token}'
                    }
                )
                if status_response.status_code != 200:
                    raise Exception(status_response.text)
                task_status = status_response.json().get('TaskStatus')

            output_uri = status_response.json().get('OutputUri')
            response = requests.get(output_uri)
            print(response)


    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    speech_file_path = Path("/tmp") / f"speech_{timestamp}.mp3"
    with open(speech_file_path, 'wb') as f:
        f.write(response.content)

    return speech_file_path
