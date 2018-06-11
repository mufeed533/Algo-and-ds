"""
 Write a Python program to test whether a passed letter is a vowel or not
"""
vowels = ['a','e','i','o','u']

letter = input()

# lower() converts uppercase letters to lowecase (in case user gives uppercase letters)
if letter.lower() in vowels:
    print("vowel")
else:
    print("not vowel")
