#!/usr/bin/env python

english_swear_words = ['ass', 'asshole', 'bitch', 'cock', 'damn', 'dick', 
                       'dumbass', 'faggot', 'fuck', 'jackass', 'motherfucker',
                       'nigger', 'pussy', 'shit', 'slut', 'tit', 'whore']

english_control_words = ['pass', 'important', 'mitten', 'bottle', 'romantic',
                         'lip', 'suggest', 'free', 'check', 'partner',
                         'funny', 'marble', 'undress', 'literate', 'riddle',
                         'energetic', 'well', 'flashy', 'mute', 'lazy',
                         'bulb', 'bolt', 'broke', 'bikes', 'wary', 'beat',
                         'steep', 'shut', 'trite', 'acrid', 'occur', 'cave',
                         'bucket', 'cars', 'stale', 'damp', 'fearful', 'shaky',
                         'play', 'covered', 'sore', 'tiny', 'faint',
                         'splendid', 'test', 'true', 'computer', 'chess',
                         'fork', 'drink', 'development']

english_words = english_swear_words + english_control_words

# Bengali and Javanese audio are broken.

target_language_map = {
    'arabic': 'ar',
    #'bengali': 'bn',
    'english': 'en-us',
    'hindi': 'hi',
    'japanese': 'ja',
    #'javanese': 'jw',
    'mandarin': 'zh-CN',
    'portuguese': 'pt',
    'russian': 'ru',
    'spanish': 'es'
    }

target_languages = target_language_map.keys()
