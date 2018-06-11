"""
Write a Python program to test whether a number is within 100 of 1000 or 2000
"""

number = int(input())

if((abs(number-1000) <= 100) or (abs(number-2000) <= 100)):
    print("True")
else:
    print("False")
