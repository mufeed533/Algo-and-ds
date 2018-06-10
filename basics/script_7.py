"""
Write a Python program to accept a filename from the user and print the extension of that
"""
# python module for handling regular expressions
import re

file_name = input()

# search() will search for the match throughout the string. () is used for grouping 
print(re.search("\.(\w+)",file_name).group(1))
