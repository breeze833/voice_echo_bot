# -*- encoding utf-8 -*-
import stt
import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Record voice and recognize')
    parser.add_argument('-l', '--lang', default='zh-tw', required=False, help='The language of the voice')
    args = parser.parse_args()
    stt.init()
    voice_data = stt.record_voice()
    text = stt.google_stt(voice_data, lang=args.lang)
    print(text)
    stt.stop()

