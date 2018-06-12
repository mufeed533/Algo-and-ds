"""
Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""

# we can use struct module from python for this purpose
import struct

print(struct.calcsize("P")*8)
