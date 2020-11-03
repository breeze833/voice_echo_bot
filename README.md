# A Simple Voice Echo Bot

This is a simple bot for demonstrating how to integrate speech-to-text and text-to-speech packages.
It records your voice, uses the Google Cloud Speech to obtain the text, sends the text to the Google Translation for synthesizing the voice, and plays the voice.
In this project, `PyAudio`, `pygame`, `pynput`, `gTTS`, and `google-cloud-speech` are used. 

## Installation

* Download the project
* Make sure you have python3
* `pip install -r < requirements.txt`

Note: you may need to install some native libraries manually.

## Configuration

* Enable Google Cloud Speech API
* Download the credentials file
* Specify where to load the credentials
  * Use environment variable `GOOGLE_APPLICATION_CREDENTIALS` to specify the file path
  * Put the file in the current working directory as `google-stt.json`
  * Put the file in your home directory as `google-stt.json`

## Usage

### Command-line: `stt-cli.py`

```
usage: stt-cli.py [-h] [-l LANG]

Record voice and recognize

optional arguments:
  -h, --help            show this help message and exit
  -l LANG, --lang LANG  The language of the voice

```

### Command-line: `tts-cli.py`

```
usage: tts-cli.py [-h] [-t TEXT] [-l LANG]

Read the given text

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  The text to be read
  -l LANG, --lang LANG  The language of the text

```

### Command-line: `echo_bot.py`

```
usage: echo_bot.py [-h] [-l LANG]

Echo what you said

optional arguments:
  -h, --help            show this help message and exit
  -l LANG, --lang LANG  The language you use

```

## Using the Cloud Text-to-Speech API

The TTS based on the Google Cloud Platform API is implemented in `stt_gcp.py`.
The corresponding comman-line programs are `tts_gcp.py` and `echo_bot_gcp.py`.
To use the API, you need the credentials file. The default name is `google-tts.json`.

