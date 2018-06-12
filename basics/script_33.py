"""
 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
"""

a = int(input())
b = int(input())
c = int(input())

sum = 0

# use python's or logic
if a == b or b == c or a == c :
    sum = 0
else:
    sum = a + b + c
print(sum)
