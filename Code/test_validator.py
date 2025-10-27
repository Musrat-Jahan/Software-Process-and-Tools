import unittest
from Validator import Validator

class MyTestCase(unittest.TestCase):
    validator = Validator()
    
    def test_valid_password(self):
        self.assertTrue(self.validator.pw_validator("8c4X!THZ4a5z"))   #valid password 

    def test_invalid_len(self):
        self.assertFalse(self.validator.pw_validator("8cCxo"))    #invalid password with len lower than 8
        self.assertFalse(self.validator.pw_validator("8c4XTH&Z4a5z1Cx1A"))   #invalid password with len greater than 15

    def test_invalid_symbol(self):
        self.assertTrue(self.validator.pw_validator("92dAff1()1"))  #valid password
        self.assertFalse(self.validator.pw_validator("8c4XTHa11"))  #doesn't contain any symbol 

    def test_invalid_uppercase(self):
        self.assertFalse(self.validator.pw_validator("m6oj4l*6r#s$"))  #doesn't contain any upper case letter

    def test_invalid_lowercase(self):
        self.assertFalse(self.validator.pw_validator("DU$8$256Q*W@V"))  #doesn't contain any lower case letter

    def test_invalid_digits(self):
        self.assertFalse(self.validator.pw_validator("DO!OPhXnqCjBR&J"))  #doesn't contain any digits

if __name__ == '__main__':
    unittest.main()
