#!/usr/bin/env python

import copy
import json
import os
import random
import shutil

from words import target_languages as languages
from words import english_swear_words as swear_words
from words import english_control_words as control_words

basedir = os.path.dirname(os.path.abspath(__file__)) + '/..'

def generate_tests():
    assert len(control_words) >= len(swear_words) * 3
    token = 0
    tests = []
    # Create a tests directory
    for language in languages:
        # Create a new list to pop from
        checklist = copy.copy(control_words)
        random.shuffle(swear_words)
        for word in swear_words:
            test = {'language': language, 'token': token, 'word': word}
            # Pick three random control words.
            random.shuffle(checklist)
            test_words = []
            for i in xrange(3):
                test_words.append(checklist.pop())
            test['controls'] = copy.copy(test_words)
            test_words.append(word)
            random.shuffle(test_words)
            test['valid_index'] = test_words.index(word)
            # Make the directory to store the files.
            _mkdirp(basedir + '/static/tests/%s/%s' % (language, token))
            # Copy the files in.
            for audio in test_words:
                source_path = basedir + '/data/audio/%s/%s/%s.mp3' % \
                    (language, 'explicit' if audio == word else 'control', audio)
                destination_path = basedir + '/static/tests/%s/%s/%s.mp3' % \
                    (language, token, test_words.index(audio))
                shutil.copyfile(source_path, destination_path)
            tests.append(test)
            token += 1
    with open(basedir + '/data/test-answers.json', 'w') as answers:
        json.dump(tests, answers, indent=4, sort_keys=True)


def _mkdirp(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

if __name__ == '__main__':
    generate_tests()
