# Write a function called check_fermat that takes four parameters: a, b, c, and n 
# and checks to see if Fermat's theorem holds. 
# If n is greater than 2 and a^n + b^n = C^n, the program should print "Holy smokes, Fermat was wrong!" 
# Otherwise print "no doesn't work."
import math

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def prompting():
    a = input("Type your value of a: \n")
    b = input("Type your value of b: \n")
    c = input("Type your value of c: \n")
    n = input("Type your value of n: \n")
    
    check_fermat(int(a), int(b), int(c), int(n))

prompting()