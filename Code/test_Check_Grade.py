import unittest
from Check_Grade import CheckGrade

class MyTestCase(unittest.TestCase):
    results = CheckGrade()

    def test_input(self):
        self.assertTrue(self.results.is_input_valid(40))
        self.assertTrue(self.results.is_input_valid(84.4))
        self.assertFalse(self.results.is_input_valid("1a1"))
        self.assertFalse(self.results.is_input_valid(111))
        self.assertFalse(self.results.is_input_valid(-1))
        self.assertFalse(self.results.is_input_valid("a"))

    def test_grade(self):
        self.assertEqual(self.results.get_grade(40), "F")
        self.assertEqual(self.results.get_grade(49.4), "F")
        self.assertEqual(self.results.get_grade(50), "P")
        self.assertEqual(self.results.get_grade(49.5), "P")
        self.assertEqual(self.results.get_grade(70), "C")
        self.assertEqual(self.results.get_grade(74.4), "C")
        self.assertEqual(self.results.get_grade(80), "D")
        self.assertEqual(self.results.get_grade(74.5), "D")
        self.assertEqual(self.results.get_grade(90), "HD")


if __name__ == '__main__':
    unittest.main()
