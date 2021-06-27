import pykakasi
# coding:utf-8
# example of pykakasis


# kana(kana): 片假
# hiragana(hira): 平假
# romaji(hepburn): 罗马音
kks = pykakasi.kakasi()


def print_result_processed(list):
    for item in list:
        print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(
            item['orig'], item['kana'], item['hira'], item['hepburn']))


def mark_sentence(sentence_breaked):
    dict = {item: kks.convert(item) for item in sentence_breaked}
    return dict


# text = 'かな漢字'
# # text = '今日'
# result = kks.convert(text)
# print_result_processed(result)
# かな: kana 'カナ', hiragana 'かな', romaji: 'kana'
# 漢字: kana 'カンジ', hiragana 'かんじ', romaji: 'kanji'

if __name__ == '__main__':
    sentence_breaked = ['昨日', 'は', '西', 'に', ',', '今日', 'は', '東', 'に']
    sentence_breaked = ['宝石', 'の', 'よう', 'に', ',', '輝い', 'て', 'いる', 'の', 'か']
    sentence_breaked = ['宝石', 'の', '宝石', 'に', ',',
                        ',', '宝石', '輝い', 'て', 'いる', 'の', ',', 'か']
    marked = mark_sentence(sentence_breaked)
    for key, value in marked.items():
        print('key:{} value:{}'.format(key, value))
