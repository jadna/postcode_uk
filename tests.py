import unittest
from postcode import *


class TestLibraryMethods(unittest.TestCase):

    def test_postcode_validity(self):
        self.assertTrue(is_postcode_valid("NR9 4QJ"))
        self.assertTrue(is_postcode_valid("CF83 1UQ"))
        self.assertTrue(is_postcode_valid("N1 8AL"))
        self.assertTrue(is_postcode_valid("PL4 8LL"))
        self.assertTrue(is_postcode_valid("CR0 8QD"))
        self.assertTrue(is_postcode_valid("RG27 9HW"))
        self.assertTrue(is_postcode_valid("HX3 0ST"))
        self.assertTrue(is_postcode_valid("EH12 7RJ"))

        self.assertFalse(is_postcode_valid("N29 422SJ"))
        self.assertFalse(is_postcode_valid("CFDS 1UQ"))
        self.assertFalse(is_postcode_valid("N13 8XL1"))
        self.assertFalse(is_postcode_valid("PX4 8L"))
        self.assertFalse(is_postcode_valid("CR2 20D"))
        self.assertFalse(is_postcode_valid("RGS7 9HW"))
        self.assertFalse(is_postcode_valid("HXSW 0ST"))
        self.assertFalse(is_postcode_valid("EH1 78J"))


if __name__ == '__main__':
    unittest.main()