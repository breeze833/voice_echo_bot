# -*- encoding: utf-8 -*-
from gtts import gTTS
from io import BytesIO
import pygame

def say(text, lang='zh-tw'):
    if text==None or text.strip()=='': return
    gtts_obj = gTTS(text, lang=lang)
    voice_mp3 = BytesIO()
    gtts_obj.write_to_fp(voice_mp3)
    voice_mp3.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(voice_mp3)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.quit()

