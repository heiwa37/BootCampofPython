'''
This is a unitest file which uses cap.py file to check whether the string given is capital in
the beginning or not
'''

import unittest
import cap

class Test_Script(unittest.TestCase):
    def test_one_word(text):
        text = "radhi"
        result = cap.cap_test(text)
        self.assertEqual(text,"Rashmi")

if __name__ == '__main__':
    unittest.main()
