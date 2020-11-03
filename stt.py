# -*- encoding: utf-8 -*-
import pyaudio
from pynput.keyboard import Listener
import os
import sys
from google.cloud import speech
from google.oauth2 import service_account

CHUNK_SIZE = 1024
RATE = 16000
pyaudio_conf = {
    'format': pyaudio.paInt16,
    'channels': 1,
    'rate': RATE,
    'frames_per_buffer': CHUNK_SIZE,
    'input': True
}

def _init_stt_context():
    p = None
    def stt_init():
        nonlocal p 
        p = pyaudio.PyAudio()
    def stt_stop():
        nonlocal p
        p.terminate()
    def recording_stream():
        nonlocal p
        return p.open(**pyaudio_conf)
    return (stt_init, stt_stop, recording_stream)

init, stop, get_recording_stream = _init_stt_context()

def _wait_anykey():
    def any_keypress(key):
        return False
    with Listener(on_press=any_keypress, suppress=True) as listener:
        listener.join()

def _get_anykey_detector():
    is_detected = False
    def on_any_keypress(key):
        nonlocal is_detected
        is_detected = True
        return False
    def start_listener():
        listener = Listener(on_press=on_any_keypress, suppress=True)
        listener.start()
    def anykey_detected():
        nonlocal is_detected
        return is_detected
    start_listener()
    return anykey_detected

def record_voice():
    print('Ready to record your voice, any key to start...', end='')
    sys.stdout.flush()
    _wait_anykey()
    print('\nStart recording, any key to stop...', end='')
    sys.stdout.flush()
    anykey_detected = _get_anykey_detector()
    stream = get_recording_stream()
    frames = []
    while not anykey_detected():
        data = stream.read(CHUNK_SIZE)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    print('\nRecording stopped.')

    return b''.join(frames)

def _get_credentials_file():
    file_env = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    file_cur = 'google-stt.json'
    file_home = os.path.join(os.path.expanduser('~'),'google-stt.json')
    if file_env!=None and os.path.exists(file_env):
        return file_env
    elif os.path.exists(file_cur):
        return file_cur
    elif os.path.exists(file_home):
        return file_home
    else:
        return None

def google_stt(voice_data, lang='zh-tw'):
    audio = speech.RecognitionAudio(content=voice_data)
    config = speech.RecognitionConfig(
        encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz = RATE,
        language_code = lang,
        enable_automatic_punctuation = True
    )
    credentials_file = _get_credentials_file()
    assert credentials_file!=None, 'Need a credentials file'
    credentials = service_account.Credentials.from_service_account_file(credentials_file)
    client = speech.SpeechClient(credentials=credentials)
    response = client.recognize(config=config, audio=audio)
    if len(response.results)==0:
        return ''
    else:
        return response.results[0].alternatives[0].transcript

