import unittest
from Area import *

class MyTestCase(unittest.TestCase):
    area = Area()
    def test_square(self):
        self.assertEqual(9,self.area.square(3))
        self.assertEqual(25,self.area.square(5))
        self.assertNotEqual(20,self.area.square(4))

    def test_rectangle(self):
        self.assertEqual(10,self.area.rectangle(5,2))
        self.assertEqual(20,self.area.rectangle(10,2))
        self.assertNotEqual(100,self.area.rectangle(4,5))        

    def test_triangle(self):
        self.assertEqual(10,self.area.triangle(4,5))
        self.assertEqual(20,self.area.triangle(8,5))
        self.assertNotEqual(30,self.area.triangle(4,5))

    def test_trapezium(self):
        self.assertEqual(25,self.area.trapezium(2,3,10))
        self.assertEqual(50,self.area.trapezium(4,6,10))
        self.assertNotEqual(100,self.area.trapezium(2,3,10))
        
if __name__ == '__main__':
    unittest.main()
