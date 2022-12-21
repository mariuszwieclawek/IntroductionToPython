"""
Wykorzystaj powyzszą klasę do stworzenia prostego kalkulatora, parsującego i wykonującego równanie podane przez
użytkownika
"""
#!/usr/bin/env python3

from ZAD14 import ComplexNumber


def main():
    print('Pierwsza liczba zespolona')
    a = int(input('Podaj czesc rzeczywista liczby zespolonej: '))
    b = int(input('Podaj czesc urojona liczby zespolonej: '))
    print('Druga liczba zespolona')
    c = int(input('Podaj czesc rzeczywista liczby zespolonej: '))
    d = int(input('Podaj czesc urojona liczby zespolonej: '))
    charac = input('Jaka operacje chcesz wykonac? (Wpisz: "+" lub "-" lub "*" lub "/"): ')
    complex_a = ComplexNumber(a, b)
    complex_b = ComplexNumber(c, d)
    if charac == '+':
        print(f'Suma liczb zespolonych ({complex_a}) + ({complex_b}) = {complex_a + complex_b}')
    elif charac == '-':
        print(f'Roznica liczb zespolonych ({complex_a}) - ({complex_b}) = {complex_a - complex_b}')


if __name__ == '__main__':
    main()
