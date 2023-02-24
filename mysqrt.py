"""
Exercise 7.1.
Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt
that takes a as a parameter, chooses a reasonable value of x, and returns an
estimate of the square root of a.
To test it, write a function named test_square_root that prints a table like this:
a   mysqrt(a)      math.sqrt(a)   diff
-   ---------      ------------   ----
1.0 1.0            1.0            0.0
2.0 1.41421356237  1.41421356237  2.22044604925e-16
3.0 1.73205080757  1.73205080757  0.0
4.0 2.0            2.0            0.0
5.0 2.2360679775   2.2360679775   0.0
6.0 2.44948974278  2.44948974278  0.0
7.0 2.64575131106  2.64575131106  0.0
8.0 2.82842712475  2.82842712475  4.4408920985e-16
9.0 3.0            3.0            0.0
The first column is a number, a;
the second column is the square root of a computed with mysqrt;
the third column is the square root computed by math.sqrt;
the fourth column is the absolute value of the difference between the two estimates.
"""
import math

def mysqrt(a, epsilon=0.001):
    """Calculates square root using Newton's method:
    https://en.wikipedia.org/wiki/Newton's_method
    
    a - positive integer < 0;
    x - estimated value, in this case a/2
    """
    x = a / 2.0
    while True:
        est_root = (x + a/x) / 2
        if abs(est_root - x) < epsilon:
            return est_root
        x = est_root

# used to find the square roots of a number using the built-in function
def square_root(a):
    x = math.sqrt(a)
    return x

def difference(a):
    d = square_root(a) - mysqrt(a)
    return d

def print_it():
    # below two print statements arranged as per requirement.
    print("numbers", " "*14, 'mysquare_root', ' '*8, 'square_root', ' '*10, "difference")
    print("-------", " " * 14, '-------------', ' ' * 8, '-----------', ' ' * 10, "----------")
    for a in range(1, 10):
        # here we are going to print square roots 1-9
        # here we are giving the 18 spaces between the one float value to another in table.
        # if there is only 15 decimal values after point, we already covered 14 position after float value, so we will give 4 spaces
        # here to do spacing between values, we just comparing float value and int value to get how much space is needed.

        print(float(a), " " * 18, f'{mysqrt(a)}', " "*18, f'{square_root(a)}',  f"{difference(a)}")

print_it()