import unittest
from straddle import encrypt, decrypt


class CrashTest(unittest.TestCase):
    def test_encrypt(self):
        # test1 normal test
        testcase = 'Prof Jump is crazy to think we can do this!'
        alpha_key = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        numeric_key = '26'
        adder_key = '38574'
        expected = 'SAAAYNORXEOE0EEAEOTFNESSJAAETNEHEAFNEAAANN'
        output = encrypt(testcase, alpha_key, numeric_key, adder_key)
        self.assertEqual(output, expected)

        # test2 all letters
        testcase = 'ABCD EFGHIJKL MNOPQRS TUVWXYZ'
        alpha_key = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        numeric_key = '26'
        adder_key = '38574'
        expected = 'ONHSHHNMEHBSSHTETQNTEHSAOAEDOSNWSRSSTO'
        output = encrypt(testcase, alpha_key, numeric_key, adder_key)
        self.assertEqual(output, expected)

        # test3 a wrong key with shorter length
        testcase = 'whatever it will be Error'
        alpha_key = 'ABC'
        numeric_key = '26'
        adder_key = '38574'
        self.assertRaises(ValueError, encrypt, testcase,
                          alpha_key, numeric_key, adder_key)

        # test3 one number in plaintext
        testcase = 'ABCD1EFGHIJKLMNOPQRSTUVWXYZ'
        alpha_key = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        numeric_key = '26'
        adder_key = '38574'
        self.assertRaises(ValueError, encrypt, testcase,
                          alpha_key, numeric_key, adder_key)

        # test4 plaintext is empty
        testcase = ''
        alpha_key = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        numeric_key = '26'
        adder_key = '38574'
        expected = 'ONHSHHNMEHBSSHTETQNTEHSAOAEDOSNWSRSSTO'
        self.assertRaises(ValueError, encrypt, testcase,
                          alpha_key, numeric_key, adder_key)

    def test_decrypt(self):
        # test1 normal test
        testcase = 'SAAAYNORXEOE0EEAEOTFNESSJAAETNEHEAFNEAAANN'
        alpha_key = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        numeric_key = '26'
        adder_key = '38574'
        expected = 'PROFJUMPISCRAZYTOTHINKWECANDOTHI'
        output = decrypt(testcase, alpha_key, numeric_key, adder_key)
        self.assertEqual(output, expected)

        # test2 all letters
        testcase = 'ONHSHHNMEHBSSHTETQNTEHSAOAEDOSNWSRSS'
        alpha_key = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        numeric_key = '26'
        adder_key = '38574'
        expected = 'ABCDEFGHIJKLMNOPQRSTUVWX'
        output = decrypt(testcase, alpha_key, numeric_key, adder_key)
        self.assertEqual(output, expected)

        # test3 empty ciphertext
        testcase = ''
        alpha_key = 'NORTHEASBCDFGIJKLMPQUVWXYZ'
        numeric_key = '26'
        adder_key = '38574'
        expected = 'ABCDEFGHIJKLMNOPQRSTUVWX'
        self.assertRaises(ValueError, decrypt, testcase,
                          alpha_key, numeric_key, adder_key)
        # test4 shorter alpha_key
        testcase = 'whatever'
        alpha_key = 'NORTHEASBCDFGI'
        numeric_key = '26'
        adder_key = '38574'
        expected = 'ABCDEFGHIJKLMNOPQRSTUVWX'
        self.assertRaises(ValueError, decrypt, testcase,
                          alpha_key, numeric_key, adder_key)
        # test5 wrong type
        testcase = 123
        alpha_key = 'NORTHEASBCDFGI'
        numeric_key = '26'
        adder_key = '38574'
        expected = 'ABCDEFGHIJKLMNOPQRSTUVWX'
        self.assertRaises(TypeError, decrypt, testcase,
                          alpha_key, numeric_key, adder_key)


def main():
    unittest.main(verbosity=3)


if __name__ == "__main__":
    main()
