"""
 Write a Python program to get the least common multiple (LCM) of two positive integers.
LCM of two number = (A*B)/GCD(a,b)
"""

a = 4
b = 5

# we can use python function approach to get the GCD value
def find_gcd(a,b):
    if a == b:
        # return value to the caller
        return a
    else:
        larger, smaller = (a,b) if a>b else (b,a)
        while True:
            remainder = larger % smaller
            if remainder == 0:
                # return value to the caller
                return smaller
            larger = smaller
            smaller = remainder

print((a//(find_gcd(a,b))*b))
