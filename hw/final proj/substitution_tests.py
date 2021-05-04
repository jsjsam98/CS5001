import unittest
from substitution import encrypt, decrypt


class CrashTest(unittest.TestCase):
    def test_encrypt(self):
        # test1 normal test
        testcase = 'Prof Jump is crazy to think we can do this!'
        keys = 'ZECTPMSHAXFVRQBWILUGKJODYN'
        expected = 'WLBMXKRWAUCLZNYGBGHAQFOPCZQTBGHAU'
        output = encrypt(testcase, keys)
        self.assertEqual(output, expected)

        # test2 a wrong key with shorter length
        testcase = 'Prof Jump is crazy to think we can do this!'
        keys = 'ZECTPMSHAXFV'
        self.assertRaises(ValueError, encrypt, testcase, keys)

        # test3 a wrong plaintext type
        testcase = 123
        keys = 'ZECTPMSHAXFVRQBWILUGKJODYN'
        self.assertRaises(TypeError, encrypt, testcase, keys)

        # test4 all letters
        testcase = 'ABCD EFGHIJKL MNOPQRS TUVWXYZ'
        keys = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        expected = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        output = encrypt(testcase, keys)
        self.assertEqual(output, expected)

        # test5 only one numeric in plaintext
        testcase = 'AB1CD EFGHIJKLMNOPQRS TUVWXYZ'
        keys = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        self.assertRaises(ValueError, encrypt, testcase, keys)

        # test6 plaintext is empty
        testcase = ''
        keys = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        self.assertRaises(ValueError, encrypt, testcase, keys)

    def test_decrypt(self):
        # test1 normal test
        testcase = 'WLBMXKRWAUCLZNYGBGHAQFOPCZQTBGHAU'
        keys = 'ZECTPMSHAXFVRQBWILUGKJODYN'
        expected = 'PROFJUMPISCRAZYTOTHINKWECANDOTHIS'
        output = decrypt(testcase, keys)
        self.assertEqual(output, expected)

        # test2 a wrong key with shorter length
        testcase = 'whatever it will raise Error'
        keys = 'ZECTPMSHAXFV'
        self.assertRaises(ValueError, encrypt, testcase, keys)

        # test3 a wrong ciphertext type
        testcase = 123
        keys = 'ZECTPMSHAXFVRQBWILUGKJODYN'
        self.assertRaises(TypeError, encrypt, testcase, keys)

        # test4 all letters
        testcase = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        keys = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        expected = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        output = encrypt(testcase, keys)
        self.assertEqual(output, expected)

        # test5 only one numeric in ciphertext
        testcase = 'AB1CDEFGHIJKLMNOPQRSTUVWXYZ'
        keys = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        self.assertRaises(ValueError, encrypt, testcase, keys)

        # test6 ciphertext is empty
        testcase = ''
        keys = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        self.assertRaises(ValueError, encrypt, testcase, keys)


def main():
    unittest.main(verbosity=3)


if __name__ == "__main__":
    main()
