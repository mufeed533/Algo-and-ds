"""
 Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)
"""
import math # math library has many useful mathematical function like squre root, power etc

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# equation of distance between two points is square_root((x1-x2)^2+(y1-y2)^2)
print(math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))) 
