#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from voicebot.stt import stt
from voicebot.tts import tts_pyttsx3 as tts
import argparse
import RPi.GPIO as GPIO
from apa102 import APA102

BUTTON = 17

def gpio_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON, GPIO.IN)

def gpio_stop():
    GPIO.cleanup()

def _init_leds():
    led_dev = None
    def _led_init():
        nonlocal led_dev
        led_dev = APA102(3)
    def _led_stop():
        led_dev.cleanup()
    def _recording_indicator(is_on):
        if is_on:
            led_dev.set_pixel(0, 255, 0, 0, 50)
        else:
            led_dev.set_pixel(0, 0, 0, 0, 50)
        led_dev.show()
    def _ready_indicator(is_on):
        if is_on:
            led_dev.set_pixel(1, 0, 255, 0, 50)
        else:
            led_dev.set_pixel(1, 0, 0, 0, 50)
        led_dev.show()
    return (_led_init, _led_stop, _ready_indicator, _recording_indicator)

def is_button_pressed():
    if GPIO.input(BUTTON):
        return False
    else:
        while not GPIO.input(BUTTON): pass
        return True

led_init, led_stop, ready_indicator, recording_indicator = _init_leds()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Echo what you said')
    parser.add_argument('-l', '--lang', required=False, default='zh-tw', help='The language you use')
    args = parser.parse_args()
    quit_terms = ['不玩了.', '不玩了。', 'Stop.', 'Stop。']

    stt.init()
    tts.init()
    gpio_init()
    led_init()

    is_echoing = True
    while is_echoing:
        voice_data = stt.record_voice(start_recording=is_button_pressed, stop_recording=is_button_pressed, ready_prompt=ready_indicator, recording_prompt=recording_indicator)
        text = stt.google_stt(voice_data, lang=args.lang)
        print('Transcript {}'.format(text))
        tts.say(text, lang=args.lang)
        is_echoing = text not in quit_terms

    stt.stop()
    tts.stop()
    gpio_stop()
    led_stop()
