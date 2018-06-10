"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

exam_st_date = (11, 12, 2014)

# python multiple assignment
date, month, year = exam_st_date

print("The examination will start from : %d / %d / %d "%(date, month, year))
