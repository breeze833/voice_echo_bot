# -*- encoding: utf-8 -*-
from google.cloud import texttospeech
from google.oauth2 import service_account
from io import BytesIO
import os
import pygame

def init():
    pygame.mixer.init()

def stop():
    pygame.mixer.quit()

def _get_credentials_file():
    file_env = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    file_cur = 'google-tts.json'
    file_home = os.path.join(os.path.expanduser('~'),'google-tts.json')
    if file_env!=None and os.path.exists(file_env):
        return file_env
    elif os.path.exists(file_cur):
        return file_cur
    elif os.path.exists(file_home):
        return file_home
    else:
        return None

def say(text, lang='zh-tw'):
    if text==None or text.strip()=='': return
    credentials_file = _get_credentials_file()
    assert credentials_file!=None, 'Need a credentials file'
    credentials = service_account.Credentials.from_service_account_file(credentials_file)
    client = texttospeech.TextToSpeechClient(credentials=credentials)
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=lang, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    voice_mp3 = BytesIO()

    try:
        voice_mp3.write(response.audio_content)
        voice_mp3.seek(0)
        
        pygame.mixer.music.load(voice_mp3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
    except Exception as e:
        print(e)

