"""
Napisz skrypt konwersji rozszerzeń plików *.jpg na *.png (uprzednio stwórz zestaw 4 plików z rozszerzeniem *.jpg)
"""
#!/usr/bin/env python3

from pathlib import Path
from PIL import Image


def convert_jpg_to_png(path):
    jpg_files = list(path.glob('**/*.jpg'))
    print(jpg_files)
    for im in jpg_files:
        convert(im)


def convert(im):
    image = Image.open(im)
    new_image = im.with_suffix('.png')
    image.save(new_image)


def main():
    dir = Path(r'C:\Users\Mariusz\Desktop\7 semestr\[PYTHON] Programowanie w języku python\images')
    convert_jpg_to_png(dir)


if __name__ == '__main__':
    main()
