#!/usr/bin/python3
'''Unitest for base'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Test Cases'''

    def test_Base(self):
        '''Test'''
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_Base1(self):
        '''Test'''
        b = Base()
        self.assertEqual(b.id, 1)

    def test_Base2(self):
        '''Test'''
        b = Base()
        self.assertEqual(b.id, 2)

if __name__ == "__main__":
    unittest.main()
