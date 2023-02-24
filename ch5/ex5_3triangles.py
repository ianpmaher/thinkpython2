# For any three lengths, simple test: 
# If any of the three lengths is greater than the sum of the other two, you cannot form a triangle. Otherwise, you can.
# If the sum of the two lengths equals the third, they form what is called a "degenerate triangle."
# Write a function named is_triangle that takes three integers as arguments, and that prints Yes or No. 

import math

def is_triangle(a, b, c):
    if a + b < c:
        print("No. That ain't no triangle, partner.")
    elif b + c < a:
        print("No. That ain't no triangle, partner.")
    elif a + c < b:
        print("No. That ain't no triangle, partner.")
    else:
        print("Yes. That's a triangle!")

def prompting():
    a = input("Type your value of length a: \n")
    b = input("Type your value of length b \n")
    c = input("Type your value of length c \n")

    is_triangle(int(a), int(b), int(c))

prompting()