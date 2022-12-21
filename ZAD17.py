"""
Napisz program proszący użytkownika o dane zawierające kilka pól (może to być np. lista zadań z opisem i terminami
wykonania czy baza recenzji filmów) i zapisujący podane dane do pliku w wybranym formacie (CSV/JSON). Przy każdym
uruchomieniu program powinien odczytywać i wyświetlać wprowadzone wcześniej dane, umożliwiać ich usunięcie (po jednym wpisie)
oraz dodanie nowych rekordów.
"""
#!/usr/bin/env python3

import csv


def data_from_user():
    name = input('Podaj imie: ')
    subname = input('Podaj nazwisko: ')
    age = input('Podaj wiek: ')

    dict_user = {
        "name": name,
        "subname": subname,
        "age": age
    }

    return dict_user


def add_user(user_data):
    with open('user_data.csv', mode='a', newline="") as user_file:
        employee_writer = csv.writer(user_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(user_data.values())
    print(user_data)


def read_user_data():
    with open('user_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)


def remove_user():
    # copy file to buffer
    buffer = []
    with open('user_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:  # copy to the buffer
            buffer.append(row)
    name_inp = input('Podaj imie aby usunac uzytkownika:')
    # remove user
    for nam in buffer:
        if name_inp in str(nam):
            buffer.remove(nam)
    # save in file
    with open('user_data.csv', mode='w', newline="") as user_file:
        employee_writer = csv.writer(user_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # TODO
        # employee_writer.writerow(row for x in buffer)


def main():
    while True:
        var = input('Wpisz opcje:\nshow - Wyswietl baze danych.\nadd - Dodaj nowego uzytkownika.\n'
                    'rem - Usun uzytkownika.\nquit - Aby wyjsc z programu.\n')
        if var == 'show':
            read_user_data()
        elif var == 'add':
            user_data = data_from_user()
            add_user(user_data)
        elif var == 'rem':
            remove_user()
        elif var == 'quit':
            break
        else:
            print('Bledny wybor opcji')


if __name__ == '__main__':
    main()
