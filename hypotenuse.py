"""
Goal: to write a function called hypotenuse.py that returns 
the length of the hypotenuse of a right triangle given the lengths
of the other two legs as arguments.
"""
import math

def hypotenuse(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    return math.sqrt(a**2 + b**2)

if __name__ == '__main__':
    print("hypotenuse is " + str(hypotenuse(3,4)))