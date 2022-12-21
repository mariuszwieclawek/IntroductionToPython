"""
Napisz skrypt sumujący dwie macierze o rozmiarach 128x128.
Wykorzystaj generator liczb losowych do wygenerowania
macierzy
"""
#!/usr/bin/env python3

import random


def matrix_sum(vector_a, vector_b):
    if len(vector_a[0]) | len(vector_a) != len(vector_b[0]) | len(vector_b):
        return -1

    result = [[0 for y in range(len(vector_a))] for x in range(len(vector_a))]
    for i in range(len(vector_a)):
        for j in range(len(vector_a)):
            result[i][j] = vector_a[i][j] + vector_b[i][j]
    return result


def main():
    col, row = 128, 128

    matrix_a = [[random.randint(-50, 50) for y in range(col)] for y in range(row)]
    matrix_b = [[random.randint(-50, 50) for y in range(col)] for y in range(row)]

    result = matrix_sum(matrix_a, matrix_b)
    print(f'matrix A: {matrix_a}')
    print(f'matrix B: {matrix_b}')
    print(f'Wartosc sumy macierzy: {result}')


if __name__ == '__main__':
    main()
