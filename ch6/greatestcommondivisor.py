# IT TURNS OUT THAT GREATEST COMMON DIVISOR IS IN THE COMMON LIBRARY NOW
# you can use math.gcd
# e.g. 
# math.gcd(3, 6)

"""The greatest common divisor (GCD) of a and b is the largest number that 
divides both of them with no remainder.
One way to find the gcd of two numbers if based on observation that if
r --> remainder when a is divided by b, then:
gcd(a, b) = gcd(b, r)
as base case, we can use gcd(a, 0) = a
write a function called gcd that takes parameters a and b and returns their greatest common divisor.
"""

def gcd_recursive(a, b):
    """Finds greatest common divisor for a and b"""
    if b == 0:
        return a
    return gcd_recursive(b, a%b)
    
print(gcd_recursive(45, 27))