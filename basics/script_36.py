"""
write a Python program to add two objects if both objects are an integer type
"""

a = 12
b = 14.0

# we can use python's isinstance fucntion to check the objcet type
if isinstance(a,int) and isinstance(b,int):
    print(a+b)
