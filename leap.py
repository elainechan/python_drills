"""
leap.py

Write a program that will take a year and report if it is a leap year.
On every year that is evenly divisible by 4.
Except every year that is evenly divisible by 100.
Unless the year is also evenly divisible by 400.
"""


def is_leap_year(year):
	if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
		return True
	elif year % 4 == 0 and year % 100 != 0:
		return True
	else:
		return False
