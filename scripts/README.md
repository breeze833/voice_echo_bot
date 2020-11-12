# Demonstration Scripts

This directory contains some demonstration scripts. Before executing the scripts, don't forget to set the python path (PYTHONPATH environment variable) so that the `voicebot` package is available to the run-time.

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

## Raspberry Pi Specific Demonstration

There are scripts that works on my Raspberry Pi based configuration. They are located in the [`respeaker/`](respeaker/) folder.

