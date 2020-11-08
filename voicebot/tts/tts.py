# -*- encoding: utf-8 -*-
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

def init():
    pass

def stop():
    pass

def say(text, lang='zh-tw'):
    if text==None or text.strip()=='': return
    gtts_obj = gTTS(text, lang=lang)
    voice_mp3 = BytesIO()
    try:
        gtts_obj.write_to_fp(voice_mp3)
        voice_mp3.seek(0)

        seg = AudioSegment.from_file(voice_mp3)
        play(seg)
    except Exception as e:
        print(e)
