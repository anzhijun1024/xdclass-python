from unittest import TestCase
import unittest
from test import MyTest


class TestMyTest(TestCase):
    def test_add(self):
        s=  MyTest()
        self.assertEqual(s.my_add(1,5),6)
if __name__ == '__main__':
    unittest.main()