'''
Shangjun Jiang
CS 5001, Fall 2020
Lab 12 -- Book

This is a unittest for Book Class
'''

from book import Book
import unittest


class CrashTest(unittest.TestCase):
    ''' Class CrashTest
    '''

    def test_init(self):
        '''
        Method -- test the constructor
        Parameters:
           self -- the current object
        '''
        book = Book("9780394800011", "Cat in the Hat", "Dr. Suess",
                    1957, "Hardcover", "catinthehat.txt")
        self.assertEqual(book.isbn, "9780394800011")
        self.assertEqual(book.title, "Cat in the Hat")
        self.assertEqual(book.author, "Dr. Suess")
        self.assertEqual(book.year, 1957)
        self.assertEqual(book.format, "Hardcover")
        self.assertEqual(book.filename, "catinthehat.txt")

    def test_get_readability_grade(self):
        '''
        Method -- test the get_readability_grade method
        Parameters:
           self -- the current object
        '''
        book = Book("9780394800011", "Cat in the Hat", "Dr. Suess",
                    1957, "Hardcover", "catinthehat.txt")
        flesh_grade = book.get_readability_grade()
        self.assertAlmostEqual(flesh_grade, '5th Grader')

    def test_get_index(self):
        '''
        Method -- test the get_index method
        Parameters:
           self -- the current object
        '''
        book = Book("9780123456789", "college", "Sam",
                    2020, "PDF", "college.txt")
        index = book.get_index()
        self.assertAlmostEqual(
            index,
            {'flesch': 1, 'invented': 1, 'a': 2,
             'simple': 1, 'tool': 1, 'to': 1, 'estimate': 1,
             'the': 1, 'legibility': 1, 'of': 1, 'document': 1,
             'without': 1, 'linguistic': 1, 'analysis': 1})


def main():
    unittest.main(verbosity=3)


main()
