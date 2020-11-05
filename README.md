# A Simple Voice Echo Bot

Here are a few sample scripts for demonstrating how to integrate speech-to-text and text-to-speech packages.
It records your voice, uses the Google Cloud Speech to obtain the text, sends the text to the Google Translation (or the Google Cloud Text to Speech) for synthesizing the voice, and plays the voice.
In this project, `PyAudio`, `pygame`, `pynput`, `gTTS`, `google-cloud-speech`, and `google-cloud-texttospeech` are used.

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

For the Google Cloud Text to Speech API, the configuration procedure is similar to the above mentioned. The difference is that the default credential name is `google-tts.json`. Of course, both APIs can be enabled under the same service account. In this case, both credentials refer to the same file.

## Usage

The sample programs are located in the `scripts/` directory. Before executing the scripts don't forget to set the python path so that the `stt`, `tts`, and `utils` packages are available to the run-time.

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

