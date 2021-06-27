import os
from fnmatch import fnmatch
import nagisa
from demo_pykakasi import mark_sentence


files = os.listdir()
format = '-lyrics'
file_reg = f'*{format}.txt'
matched = [file for file in files
           if fnmatch(file, file_reg)]


def translate_word(word):
    orig = word['orig']
    hira = word['hira']
    roma = word['hepburn']
    if orig == hira:
        return orig
    else:
        return f'{orig}({roma})'


def process_marked_words(words_marked):
    words = [translate_word(word) for word in words_marked]
    result = ''.join(words)
    return result


def separate_line(line):
    tagged = nagisa.tagging(line)
    result = tagged.words
    # print(f'tagged:{tagged}')
    # print(f'tagged words:{result}')
    return result


def translate_string(str):
    words = separate_line(str)
    dictionary = mark_sentence(words)
    result = [process_marked_words(dictionary[item]) for item in words]
    return ' '.join(result)


for lyric_file in matched:
    content = open(lyric_file, 'r', encoding='UTF-8').readlines()
    whole = '.'.join([item.strip('\n') for item in content])

    name = os.path.splitext(lyric_file)[0].strip(format)
    print('process lyrics for {} ...'.format(name))

    translated = translate_string(whole)
    result = translated.split('.')
    for index, line in enumerate(result):
        print('[{}]:{}'.format(index, line.strip(' ')))
