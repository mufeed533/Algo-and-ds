"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
# python datetime module helps to manipulate date and time
import datetime

now = datetime.datetime.now()

#print the date and time as specified(format)
print(now.strftime("%y-%m-%d %H:%M:%S"))
