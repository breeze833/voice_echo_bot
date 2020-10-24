# A Simple Voice Echo Bot

This is a simple bot. It records your voice, uses the Google Clod Speech to obtain the text, sends the text to the Google Translation for synthesizing the voice, and plays the voice.

## Installation

* Download the project
* Makesure you have python3
* `pip install -r < requirements.txt`

Note: you may need to install some native libraries manually.

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
