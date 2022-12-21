"""
Napisz skrypt zliczający ilość plików w katalogu /dev, skorzystaj
ze standardowej biblioteki - os
"""
#!/usr/bin/env python3

import pathlib


def files_count(path):
    counter = 0
    for file in pathlib.Path(path).iterdir():
        if file.is_file():
            counter += 1
    print(f'Liczba plikow w katalogu {path}: {counter}')


def main():
    dir = r'C:\Users\Mariusz\Desktop\7 semestr'
    files_count(dir)


if __name__ == '__main__':
    main()

