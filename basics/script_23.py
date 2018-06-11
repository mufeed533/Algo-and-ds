"""
Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2
"""

string = "abcd"
number  = int(input())

if len(string) >= 2:
    print(string[:2]*number)
else:
    print(string*number)
