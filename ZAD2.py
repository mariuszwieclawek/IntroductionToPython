"""
Napisz skrypt realizujący funkcję zamka szyfrowego. Prosi
o podanie kodu i następnie sprawdza czy jest on zgodny z
wcześniej wprowadzonym kodem
"""
#!/usr/bin/env python3

def password():
    print('Podaj szyfr:')
    user_password = input()
    print('Zaszyfrowano. Podaj znowu szyfr:')
    input_password = input()
    if input_password == user_password:
        print('Otwarto zamek')
    else:
        print('Bledny szyfr')


if __name__ == '__main__':
    password()
