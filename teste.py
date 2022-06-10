import unittest
import postcode
import os, sys



def test_formatting(code):
    nice = postcode.is_postcode_valid(code)
    print(nice)



if __name__ == '__main__':

    test_formatting('B1 1H')