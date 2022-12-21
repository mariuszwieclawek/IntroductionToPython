"""
Napisz skrypt obliczający wartość iloczynu dwóch wektorów:
a = [1, 2, 12, 4], b = [2, 4, 2, 8], tzw. iloczyn skalarny wektorów
"""
#!/usr/bin/env python3

import random


def scalar_product(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        return -1

    prod = 0
    for x in range(len(vector_a)):
        prod += vector_a[x] * vector_b[x]

    return prod


def main():
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    prod = scalar_product(a, b)
    print(f'Wartosc iloczynu skalarnego {prod}')


if __name__ == '__main__':
    main()
