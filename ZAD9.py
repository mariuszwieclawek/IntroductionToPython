"""
Napisz skrypt sortujący liczby malejąco. Wygeneruj losowo 50
liczb - wykorzystąj standardową funkcje do losowania. Z wbudowanej funkcji sortującej korzystaj tylko w celu weryfikacji
wyników
"""
#!/usr/bin/env python3

import random


def sort_number(number_list):
    for i in range(0, len(number_list) - 1):
        for j in range(0, (len(number_list) - 1)):
            if number_list[j] > number_list[j+1]:
                temp = number_list[j]
                number_list[j] = number_list[j+1]
                number_list[j+1] = temp

    return number_list


def main():
    numbers = []
    for x in range(0, 50):
        numbers.append(random.randint(-50, 50))
    sorted_numbers = sort_number(numbers)
    print(sorted_numbers)


if __name__ == '__main__':
    main()
