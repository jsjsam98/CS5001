'''
Shangjun Jiang
CS 5001, Fall 2020
Lab 14 -- frequency_sort_tests
'''

import unittest
from frequencysort import sort


class CrashTest(unittest.TestCase):
    def test_sort(self):
        testcase = [[3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8, 8], [
            1, 2, 2, 3, 3, 3], [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]]
        expected = [[8, 8, 8, 8, 3, 3, 3, 1, 1, 1, 6, 7], [
            3, 3, 3, 2, 2, 1], [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]]
        index = 0
        done = False
        while not done:
            sort(testcase[index])
            self.assertEqual(testcase[index], expected[index])
            index += 1
            if index == len(testcase):
                done = True


def main():
    unittest.main(verbosity=3)


if __name__ == "__main__":
    main()
