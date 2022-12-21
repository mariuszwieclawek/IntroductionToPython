#!/usr/bin/env python3

import unittest
import random
from ZAD9 import sort_number


class SortTest(unittest.TestCase):
    def test_sort(self):
        testlist = [1, 6, 2, 8, 4, 1, 0, 3, 6, 2]
        expected = testlist.copy()
        expected.sort()
        self.assertListEqual(sort_number(testlist), expected)

    def test_letter(self):
        testlist = [1, 6, 2, "x", 4, 1, 0, 3, 6, 2]
        expected = False
        # result = sort_number(testlist)
        # self.assertEqual(result, expected)
        with self.assertRaises(expected_exception=TypeError):
            sort_number(testlist)

    def test_series(self):
        # create data to sort
        len_of_list = 8
        number_of_subtests = 5
        matrix = [[random.randint(-5, 5) for x in range(len_of_list)] for y in range(number_of_subtests)]
        # start subtesting
        for iter in range(0, number_of_subtests):
            with self.subTest(i=iter):
                expected = matrix[iter]
                expected.sort()
                self.assertListEqual(sort_number(matrix[iter]), expected)



    # def test_sth(self):
    #     pass
    #     #GIVEN
    #     #then
    #     #expected


def main():
    SortTest.test_sort()


if __name__ == '__main__':
    unittest.main()