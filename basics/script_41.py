"""
Write a Python program to check whether a file exists
"""

import os # os module contains several functions to deal with system

file_name = "script_40.py"

# os.path.isfile check whether a file is present in the specified path or not, try to give full path of the file
print(os.path.isfile(file_name))
