# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:33:25 2021

@author: Alessandro
"""

# Python program for the extended Euclidean algorithm
def extended_euclid(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclid(b % a, a)
        return gcd, y - (b // a) * x, x
 
 
if __name__ == '__main__':
 
    gcd, x, y = extended_euclid(300, 51)
    print("The GCD is", gcd)
    print(f"x = {x}, y = {y}")