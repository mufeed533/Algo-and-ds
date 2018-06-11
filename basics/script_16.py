"""
Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
"""
number = int(input())

if number<17:
    print(17-number)
else:
    # abs() function gives absolute value of a number
    print(abs(17-number)*2)
