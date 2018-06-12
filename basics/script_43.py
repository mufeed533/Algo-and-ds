"""
Write a Python program to get OS name, platform and release information
"""
# we can use os module for os related problems
import os

# we can use platform module for platform related problems
import platform

print("Os name : ", os.name)
print("platform :", platform.system())
print("release information :", platform.release())
