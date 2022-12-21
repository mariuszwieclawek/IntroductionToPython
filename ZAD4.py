"""
Napisz rekurencyjne przejście drzewa katalogów i wypisanie
plików, które znajdują się w eksplorowanej strukturze
"""
#!/usr/bin/env python3


from pathlib import Path


def print_files_in_tree(path):
    print(f'Pliki znajdujące się w sciezce "{path}":')
    for x in path.iterdir():
        if x.is_file():
            print(x)
    print('\n')
    new_path = path.parent
    if new_path == path:
        return
    print(new_path)
    print_files_in_tree(new_path)


def main():
    dir = Path(r'C:\Users\Mariusz\Desktop\7 semestr')
    print_files_in_tree(dir)


if __name__ == '__main__':
    main()
