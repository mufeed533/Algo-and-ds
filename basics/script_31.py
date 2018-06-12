"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers
The Euler theorem to find GCD of two numbers
1. If both numbers are equal GCD is any of the number
2. else set larger number as the smaller number and smaller as the remainder of larger divided by smaller
3. if remainder is zero GCD is the smaller number
4. repeat
"""
a = int(input())
b = int(input())

if a == b:
    print(a)
else:
    # python short cut for unpacking multiple variables
    larger,smaller = (a,b) if a > b else (b,a)

    # infinte while loop
    while True:
        remainder = larger % smaller
        if remainder == 0:
            print(smaller)
            break
        larger = smaller
        smaller = remainder
