#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from stt import stt
from tts import tts_gcp as tts
import time
import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Echo what you said')
    parser.add_argument('-l', '--lang', required=False, default='zh-tw', help='The language you use')
    args = parser.parse_args()
    quit_terms = ['不玩了.', '不玩了。', 'Stop.', 'Stop。']

    stt.init()
    tts.init()

    is_echoing = True
    while is_echoing:
        voice_data = stt.record_voice()
        text = stt.google_stt(voice_data, lang=args.lang)
        print('Transcript {}'.format(text))
        time.sleep(2)
        tts.say(text, lang=args.lang)
        if text in quit_terms:
            is_echoing = False

    stt.stop()
    tts.stop()
