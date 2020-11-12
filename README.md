# A Simple Voice Echo Bot

Here are a few sample scripts and modules for demonstrating how to integrate speech-to-text and text-to-speech packages.
It records your voice, uses the Google Cloud Speech to obtain the text, sends the text to the Google Translation (or the Google Cloud Text to Speech) for synthesizing the voice, and plays the voice.
In this project, `PyAudio`, `pydub`, `pynput`, `gTTS`, `google-cloud-speech`, and `google-cloud-texttospeech` are used.

In addition to the cloud-based TTS, we also use the `pyttsx3` to synthesize the speech locally. The backend depends on the platform. For example, it is eSpeak on Linux.

## Installation

* Download the project
* Make sure you have python3
* `pip install -r < requirements.txt`

Note 1: You may need to install some native libraries manually.
Note 2: On Raspberry Pi, sometimes assertion failure would occur. It is caused by a bug in the PortAudio. Without fixing the library, installing pulseaudio or jackd is a workaround.

## Configuration

* Enable Google Cloud Speech API
* Download the credentials file
* Specify where to load the credentials
  * Use environment variable `GOOGLE_APPLICATION_CREDENTIALS` to specify the file path
  * Put the file in the current working directory as `google-stt.json`
  * Put the file in your home directory as `google-stt.json`

For the Google Cloud Text to Speech API, the configuration procedure is similar to the above mentioned. The difference is that the default credential name is `google-tts.json`. Of course, both APIs can be enabled under the same service account. In this case, both credentials refer to the same file.

## Usage

The sample programs are located in the `scripts/` directory. Please refer to the README file in the directoryi to learn how to use them.


