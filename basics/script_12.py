"""
Write a Python program to print the calendar of a given month and year.
"""
# calender module from python can be helpful for manipulating clander related things
import calendar

month = int(input())
year = int(input())

print(calendar.month(month,year))
