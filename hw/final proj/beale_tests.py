import unittest
from beale import encrypt, decrypt


class CrashTest(unittest.TestCase):
    def test_encrypt(self):
        # book.txt is for test
        # test1 all letters
        testcase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        keys = 'book.txt'
        seed = 10
        expected = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 \
15 16 17 18 19 20 21 22 23 24 25 26'
        output = encrypt(testcase, keys, seed)
        self.assertEqual(output, expected)

        # test2 empty plaintext
        testcase = ''
        keys = 'book.txt'
        seed = 10
        self.assertRaises(ValueError, encrypt, testcase, keys, seed)

        # test3 wrong plaintext
        testcase = 'A1CDEFGHIJKLMNOPQRSTUVWXYZ'
        keys = 'book.txt'
        seed = 10
        expected = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 \
14 15 16 17 18 19 20 21 22 23 24 25'
        self.assertRaises(ValueError, encrypt, testcase, keys, seed)

        # test4 wrong seed type
        testcase = 'A1CDEFGHIJKLMNOPQRSTUVWXYZ'
        keys = 'book.txt'
        seed = '10'
        expected = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 \
14 15 16 17 18 19 20 21 22 23 24 25'
        self.assertRaises(TypeError, encrypt, testcase, keys, seed)

        # test5 repeated letters
        testcase = 'AABBCCCDDD'
        keys = 'book.txt'
        seed = 10
        expected = '1 1 2 2 3 3 3 4 4 4'
        output = encrypt(testcase, keys, seed)
        self.assertEqual(output, expected)

    def test_decrypt(self):
        # test1 all letters
        testcase = '1 2 3 4 5 6 7 8 9 10 11 12 13 \
14 15 16 17 18 19 20 21 22 23 24 25 26'
        keys = 'book.txt'
        expected = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        output = decrypt(testcase, keys)
        self.assertEqual(output, expected)

        # test2 empty ciphertext
        testcase = ''
        keys = 'book.txt'
        seed = 10
        self.assertRaises(ValueError, encrypt, testcase, keys, seed)

        # test3 repeated letters
        testcase = '1 2 2 3 3 4 4 4'
        keys = 'book.txt'
        expected = 'ABBCCDDD'
        output = decrypt(testcase, keys)
        self.assertEqual(output, expected)

        # test4 wrong ciphertext type
        testcase = 123
        keys = 'book.txt'
        seed = 10
        self.assertRaises(TypeError, encrypt, testcase, keys, seed)


def main():
    unittest.main(verbosity=3)


if __name__ == "__main__":
    main()
