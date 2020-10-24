# -*- encoding utf-8 -*-
import pyaudio
from pynput.keyboard import Listener
import sys
import os
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

def wait_anykey():
    listener = None
    def any_keypress(key):
        nonlocal listener
        listener.stop()
    listener = Listener(on_press=any_keypress, suppress=True)
    with listener:
        listener.join()

def get_anykey_detector():
    is_detected = False
    listener = None
    def any_keypress(key):
        nonlocal is_detected
        nonlocal listener
        is_detected = True
        listener.stop()
    def start_listener():
        nonlocal listener
        listener = Listener(on_press=any_keypress, suppress=True)
        listener.start()
    def anykey_detected():
        nonlocal is_detected
        return is_detected
    start_listener()
    return anykey_detected

def record_voice():
    print('Ready to record your voice, any key to start...', end='')
    sys.stdout.flush()
    wait_anykey()
    print('\nStart recording, any key to stop...', end='')
    sys.stdout.flush()
    anykey_detected = get_anykey_detector()
    stream = get_recording_stream()
    frames = []
    while not anykey_detected():
        data = stream.read(CHUNK_SIZE)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    print('\nRecording stopped.')

    return b''.join(frames)

def get_credentials_file():
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
        language_code = lang
    )
    credentials_file = get_credentials_file()
    assert credentials_file!=None, 'Need a credentials file'
    credentials = service_account.Credentials.from_service_account_file(get_credentials_file())
    client = speech.SpeechClient(credentials=credentials)
    response = client.recognize(config=config, audio=audio)
    if len(response.results)==0:
        return ''
    else:
        return response.results[0].alternatives[0].transcript

