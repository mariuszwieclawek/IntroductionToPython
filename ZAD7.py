"""
Napisz skrypt zmieniający w podanym ciągu wejściowym
(wybierz kilka plików z repozytorium: Tekstowego) następujące
słowa : i, oraz, nigdy, dlaczego na następujący zestaw słów : oraz,
i, prawie nigdy, czemu. Zalecaną strukturą jest słownik.
"""
#!/usr/bin/env python3

from pathlib import Path
from PIL import Image


def delete_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    print(text)
    new_text = replace_words_from_text(text)
    print(new_text)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)


def replace_words_from_text(text):
    word_dict = {
        'i' : 'oraz',
        'oraz' : 'i',
        'nigdy' : 'prawie nigdy',
        'dlaczego' : 'czemu'
    }

    text_list = text.split(' ')

    result = [word_dict[x] for x in text_list]
    result = []
    for x in text_list:
        try:
            result.append(word_dict[x])
        except KeyError:
            result.append(x)


    key_list = word_dict.keys()
    new_list = []
    print(text_list)
    for word in text_list:
        for key in key_list:
            if word == key:
                word = word_dict[word]
        new_list.append(word)
    print(new_list)
    return text


def main():
    dir = Path(r'C:\Users\Mariusz\Desktop\7 semestr\[PYTHON] Programowanie w języku python\text\zamiana.txt')
    delete_words(dir)


if __name__ == '__main__':
    main()
