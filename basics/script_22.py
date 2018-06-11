"""
 Write a Python program to count the number 4 in a given list
"""
number_list = [1,2,3,4,4,5,4,5]

# we can use the count() function from list for this
print(number_list.count(4))

"""
alternative way

count = 0
for i in number_list:
    if i == 4:
        count += 1
print(count)
""""
