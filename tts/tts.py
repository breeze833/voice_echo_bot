# -*- encoding: utf-8 -*-
from gtts import gTTS
from io import BytesIO
import pygame

def init():
    pygame.mixer.init()

def stop():
    pygame.mixer.quit()

def say(text, lang='zh-tw'):
    if text==None or text.strip()=='': return
    gtts_obj = gTTS(text, lang=lang)
    voice_mp3 = BytesIO()
    try:
        gtts_obj.write_to_fp(voice_mp3)
        voice_mp3.seek(0)

        pygame.mixer.music.load(voice_mp3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
    except Exception as e:
        print(e)
