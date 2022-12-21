"""
Napisz skrypt obliczający pierwiastki równania kwadratowego
w postaci : y = ax2+bx+c. Wejściem skryptu są wartości: a, b, c
"""
#!/usr/bin/env python3

import math


def square_equation(a, b, c):
    delta = math.pow(b, 2) - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / 2 * a
        x2 = (-b + math.sqrt(delta)) / 2 * a
        print(f'For y = {a}x^2 + {b}x + {c} : Delta > 0, solution: x1 = {x1}, x2 = {x2}')
    elif delta == 0:
        x0 = (-b / 2 * a)
        print(f'For y = {a}x^2 + {b}x + {c} : Delta = 0, solution: x0 = {x0}')
    else:
        print(f'For y = {a}x^2 + {b}x + {c} : Delta < 0, no solution')


def main():
    square_equation(2, 2, 2)
    square_equation(2, 4, 2)
    square_equation(2, 6, 2)


if __name__ == '__main__':
    main()
