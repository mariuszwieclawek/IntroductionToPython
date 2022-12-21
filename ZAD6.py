"""
Napisz skrypt usuwający z wejściowego ciągu tekstowego
(wybierz kilka plików z repozytorium: Tekstowego) następujące
słowa : się, i, oraz, nigdy, dlaczego
"""
#!/usr/bin/env python3

from pathlib import Path
from PIL import Image


def delete_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    print(text)
    new_text = delete_words_from_text(text)
    print(new_text)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)


# do zrobienia jeszcze zeby nie usuwalo wyrazow w slowie np nigdy -> ngdy
def delete_words_from_text(text):
    word_list_to_delete = ['się', 'i', 'oraz', 'nigdy', 'dlaczego']
    for word in word_list_to_delete:
        text = text.replace(word, '')
    return text


def main():
    dir = Path(r'C:\Users\Mariusz\Desktop\7 semestr\[PYTHON] Programowanie w języku python\text\text.txt')
    delete_words(dir)


if __name__ == '__main__':
    main()
