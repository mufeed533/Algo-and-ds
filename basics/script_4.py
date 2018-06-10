"""
 Write a Python program which accepts the radius of a circle from the user and compute the area.
"""
import math

# read input from user and convert it into floar because console input will be always string
radius = float(input())

# area eq - pi*radius^2 . pow is the power fucntion in python
area = math.pi*pow(radius,2)

# print the area with 3 digits after decimal
print("%0.3f" % area)
