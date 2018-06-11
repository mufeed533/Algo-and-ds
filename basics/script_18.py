"""
Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
"""
a = int(input())
b = int(input())
c = int(input())

# python shorcut for assignment operation 
if(a == b == c):
    print(3*a)
else:
    print(a+b+c)
