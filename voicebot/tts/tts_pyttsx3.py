# -*- encoding: utf-8 -*-
import pyttsx3

_engine = None

def init():
    global _engine
    _engine = pyttsx3.init()

def stop():
    pass

def say(text, lang='zh-tw'):
    if text==None or text.strip()=='': return
    _engine.setProperty('voice', lang[:2]) # This is a dirty hack, only use the first two letters of the language code
    _engine.say(text)
    _engine.runAndWait()
