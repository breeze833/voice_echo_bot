#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import argparse
import tts

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Read the given text')
    parser.add_argument('-t', '--text', default='你好，這是一段語音轉文字測試', required=False, help='The text to be read')
    parser.add_argument('-l', '--lang', default='zh-tw', required=False, help='The language of the text')
    args = parser.parse_args()
    tts.init()
    tts.say(args.text, args.lang)
    tts.stop()
