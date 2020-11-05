# -*- encoding: utf-8 -*-
from google.cloud import texttospeech
from io import BytesIO
import pygame
from utils.gcp_utils import get_credentials

def init():
    pygame.mixer.init()

def stop():
    pygame.mixer.quit()

def say(text, lang='zh-tw'):
    if text==None or text.strip()=='': return
    client = texttospeech.TextToSpeechClient(credentials=get_credentials('google-tts.json'))
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

