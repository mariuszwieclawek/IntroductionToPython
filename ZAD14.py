"""
Zdefiniuj klasę reprezentującą liczby zespolone (wraz z funkcjami na nich działającymi np. dodawanie, odejmowanie itd.)
"""
#!/usr/bin/env python3

from cmath import sqrt


class ComplexNumber(object):
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return ComplexNumber(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return ComplexNumber((self.re * other.re) - (self.im * other.im),
                       (self.im * other.re) + (self.re * other.im))

    def __truediv__(self, other):
        r = (other.real**2 + other.imag**2)
        return ComplexNumber((self.re*other.real - self.im*other.imag)/r,
            (self.im*other.real + self.re*other.imag)/r)

    def __abs__(self):
        new = (self.re**2 + (self.im**2)*-1)
        return ComplexNumber(sqrt(new.real))

    def __str__(self):
        if self.im >= 0:
            return f'{self.re} + {self.im}j'
        else:
            return f'{self.re} {self.im}j'


def main():
    a = ComplexNumber(3, 2)
    b = ComplexNumber(4, 6)
    print(f'Suma liczb zespolonych ({a}) + ({b}) = {a + b}')
    print(f'Roznica liczb zespolonych ({a}) - ({b}) = {a - b}')


if __name__ == '__main__':
    main()
