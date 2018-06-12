"""
. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
"""
a = int(input())
b = int(input())

# python shorcut for if condition 
print(20 if 15 <= (a+b) <= 20 else (a+b))
