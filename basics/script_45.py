"""
Write a python program to call an external command in Python.
"""
# subprocess module is used to create new processes in a python program
import subprocess

print(subprocess.call(["ls","-l"]))
