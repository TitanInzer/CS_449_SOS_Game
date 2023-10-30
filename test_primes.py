# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:04:38 2023

@author: codyi
"""

from primes import is_prime

def test_five_is_prime():
    assert is_prime(5) == True
    
def test_four_is_prime():
    assert is_prime(4) == False
    
def test_one_is_prime():
    assert is_prime(1) == False