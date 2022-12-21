#!/usr/bin/env python3

import random


def matrix_product(vector_a, vector_b):
    if len(vector_a[0]) != len(vector_b) and len(vector_b[0]) | len(vector_a):
        return -1

    result = [[0 for y in range(len(vector_a))] for x in range(len(vector_a))]
    for i in range(len(vector_a[0])):
        for j in range(len(vector_b)):
            summ = 0
            for k in range(len(vector_b)):
                summ += vector_a[i][k] * vector_b[k][j]
            result[i][j] = summ
    return result


def main():
    col, row = 8, 8

    matrix_a = [[random.randint(-3, 3) for y in range(col)] for y in range(row)]
    matrix_b = [[random.randint(-3, 3) for y in range(col)] for y in range(row)]

    result = matrix_product(matrix_a, matrix_b)
    print(f'matrix A: {matrix_a}')
    print(f'matrix B: {matrix_b}')
    print(f'Wartosc iloczynu macierzy: {result}')


if __name__ == '__main__':
    main()
