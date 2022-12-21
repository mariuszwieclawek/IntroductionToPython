"""
Napisz skrypt, który pyta o imię, nazwisko i rok urodzenia
(powinny być podane w jednej linii)
"""
#!/usr/bin/env python3

if __name__ == '__main__':
    def person():
        print('Podaj imie, nazwisko oraz rok urodzenia:')
        person_input = input()
        person_data = person_input.split(' ')
        person_information = {
            "imie": person_data[0],
            "nazwisko": person_data[1],
            "data urodzenia": person_data[2]
        }
        print(person_information)
    person()
