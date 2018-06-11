"""
Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged
"""
import re
string = "Hi this a good example"
if re.match("Is", string):
    print(string)
else:
    print("Is "+string)
