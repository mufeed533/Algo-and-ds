"""
manually create a calander without using calander moduleself.
Given the no of days in the month and the day of the week to start the month
"""

days = int(input("Please enter number of days: "))
day_of_week = input("Please enter the first day of the week: ")

def print_calendar(days,day_of_week):

    print("S  M  T  W  T  F  S")   # print heading
    day = {                         # dictionary to connect day and its index
            "s" : 1,"m" : 2,"t" : 3,"w" : 4,"th": 5,"f" : 6,"sun": 7
          }

    i = 1
    num = 1

    # loop to print the first raw of the calander. This raw is seperated from remainig raw because the first raw may have empty spaces.
    while i <= 7:
        if i < day[day_of_week]:
            print(" ", end = "  ")
        else:
            print(num, end = "  ")
            num += 1
        i += 1
    print()


    # loop to print the remaining days
    counter = 1
    while num <= days:
        print(num, end = "   ")
        if counter % 7 == 0:
            print()
        num += 1
        counter += 1

print_calendar(days,day_of_week)
