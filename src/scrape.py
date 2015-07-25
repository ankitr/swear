#!/usr/bin/env python

from __future__ import print_function

import io
import json
import re
import requests

from words import english_words
from words import english_swear_words
from words import target_language_map
from words import target_languages

TEXT_URL = ('http://translate.googleapis.com/translate_a/single?'
                'client=gtx&sl=%s&tl=%s&dt=t&q=%s')
TTS_URL = 'http://translate.google.com/translate_tts?ie=UTF-8&q=%s&tl=%s'

dictionary = {}

def scrape_text():
    # Get text samples for all languages
    # TODO(ankitr): Make this less janky and handle for Google's rate-limiting
    for language in target_languages:
        print(language)
        dictionary[language] = {}
        for english_word in english_words:
            response = requests.get(TEXT_URL % ('en', target_language_map[language],
                                                  english_word))
            if response.status_code != requests.codes.ok:
                print('Skipping %s, %s' % (english_word, language))
                break
            # JSON Parsing doesn't work (?)
            #print(response.json()[0][0][0])
            foreign_word = re.search(r'".*?"', response.text).group().strip('"')
            print(foreign_word)
            dictionary[language][english_word] = foreign_word
    with io.open('data/dictionary.json', 'w', encoding='utf8') \
        as dictionary_store:
        # Python 2 bug where ensure_ascii occasionally passes type str doesn't
        # allow up to use json.dump :-(
        data = json.dumps(dictionary, ensure_ascii=False, encoding='utf8')
        dictionary_store.write(unicode(data))

def get_audio():
    # TODO(ankitr): figure out why bengali and javanese failed
    with io.open('data/dictionary.json', 'r', encoding='utf8') \
        as dictionary_source:
        a = dictionary_source.read()
        dictionary = _unicodify(json.loads(a, encoding='utf8'))
    for language in target_languages:
        print(language)
        for english_word in english_words:
            outfile_name = 'data/audio/%s/%s/%s.mp3' \
                % (language, 'explicit' if english_word in english_swear_words \
                    else 'control', english_word)
            response = requests.get(TTS_URL \
                % (dictionary[language][english_word],
                    target_language_map[language]))
            if response.status_code != requests.codes.ok:
                print('Skipping %s, %s' % (english_word, language))
                break
            with open(outfile_name, 'wb') as outfile:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        # Clears out keep-alives, etc.
                        outfile.write(chunk)
                        outfile.flush()
            print(english_word)


def _unicodify(input):
    if isinstance(input, dict):
        return {_unicodify(key):_unicodify(value) for key,value
                   in input.iteritems()}
    elif isinstance(input, list):
        return [_unicodify(element) for element in input]
    else:
        return input.encode('utf8')

if __name__ == '__main__':
    #scrape_text()
    get_audio()
