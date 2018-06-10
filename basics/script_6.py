"""
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
"""

# read the input and seperate them by comma
numbers = input().split(',')

# convert them to list of integers
list_numbers = [int(i) for i in numbers]

# convert the list into tuple
tuple_numbers = tuple(list_numbers)
print(list_numbers)
print(tuple_numbers)
