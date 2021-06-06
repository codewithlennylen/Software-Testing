from math import pi
from typing import Type

def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number")
        
    if radius < 0:
        raise ValueError("The radius cannot be negative")

    return pi*(radius**2)

# print(circle_area(7))