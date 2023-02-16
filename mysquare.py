import turtle
bob = turtle.Turtle()
print(bob)

def square(t, length):
    for i in range (4):
        t.fd(length)
        t.lt(90)

square(bob, 200)

turtle.mainloop()