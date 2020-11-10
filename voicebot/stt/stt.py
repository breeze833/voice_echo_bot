# -*- encoding: utf-8 -*-
import pyaudio
import threading
from google.cloud import speech
from voicebot.utils.gcp_utils import get_credentials

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

def is_enter_pressed(msg):
    t = None
    def _myinput():
        input(msg)
    def _is_enter_pressed():
        nonlocal t
        if t: 
            if t.is_alive():
                return False
            else:
                t = None
                return True
        else:
            t = threading.Thread(target=_myinput)
            t.start()
            return False

    return _is_enter_pressed

def record_voice(start_recording=is_enter_pressed('Press <Enter> to start...'), stop_recording=is_enter_pressed('Press <Enter> to stop...')):
    """
    The function to get the recorded voice.

    Arguments:
    start_recording -- the non-blocking function that returns True if the recorder can be started.
    stop_recording -- the non-blocking function that returns True if the recorder should be stopped.
    """
    print('\nReady to start recording...', end='')
    while not start_recording():
        pass
    print('\nRecording started')
    stream = get_recording_stream()
    frames = []
    while not stop_recording():
        data = stream.read(CHUNK_SIZE)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    print('\nRecording stopped.')

    return b''.join(frames)

def google_stt(voice_data, lang='zh-tw'):
    audio = speech.RecognitionAudio(content=voice_data)
    config = speech.RecognitionConfig(
        encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz = RATE,
        language_code = lang,
        enable_automatic_punctuation = True
    )
    client = speech.SpeechClient(credentials=get_credentials('google-stt.json'))
    response = client.recognize(config=config, audio=audio)
    if len(response.results)==0:
        return ''
    else:
        return response.results[0].alternatives[0].transcript

