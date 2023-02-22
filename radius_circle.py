import math

def radius(xc, yc, xp, yp):
    dx = xc - xp
    dy = yc - yp
    return radius

def cirle_area(radius):
    a = math.pi * radius**2
    return math.pi * radius**2


"""
def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result
"""

def circle_area(xc, yc, xp, yp):
    return area(radius(xc, yc, xp, yp))

print(radius(2, 2, 2, 2))