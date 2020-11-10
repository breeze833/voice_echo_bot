#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from voicebot.stt import stt
from voicebot.tts import tts_gcp as tts
import argparse
import RPi.GPIO as GPIO

BUTTON = 17

def gpio_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON, GPIO.IN)

def gpio_stop():
    GPIO.cleanup()

def is_button_pressed():
    if GPIO.input(BUTTON):
        return False
    else:
        while not GPIO.input(BUTTON): pass
        return True

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Echo what you said')
    parser.add_argument('-l', '--lang', required=False, default='zh-tw', help='The language you use')
    args = parser.parse_args()
    quit_terms = ['不玩了.', '不玩了。', 'Stop.', 'Stop。']

    stt.init()
    tts.init()
    gpio_init()

    is_echoing = True
    while is_echoing:
        voice_data = stt.record_voice(start_recording=is_button_pressed, stop_recording=is_button_pressed)
        text = stt.google_stt(voice_data, lang=args.lang)
        print('Transcript {}'.format(text))
        tts.say(text, lang=args.lang)
        is_echoing = text not in quit_terms

    stt.stop()
    tts.stop()
    gpio_stop()
