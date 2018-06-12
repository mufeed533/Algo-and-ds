"""
 Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
"""

amt = 1000
int = 3.5
years = 7

print(round(amt*((1+(0.01*int)) ** years))  )
