"""
The Ackermann function as Python function. A(m,n)
    See http://en.wikipedia.org/wiki/Ackermann_function
m and n have to be nonnegative integers.

This link shows complexity: https://gfredericks.com/things/arith/ackermann


"""

from __future__ import print_function, division


def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
    See http://en.wikipedia.org/wiki/Ackermann_function
    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


print(ackermann(3, 4))