year = int(input("Please enter the year:-"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is leap Year.")
else:
    print(f"{year} is not a leap year")

Logic:-
#year % 4 == 0 > logic is :- after devide reminder is 0
# and year % 100 != 0 > logic is :- It's century year but not a leap year
# or year % 400 == 0: > logic is :- It's devisible by 400 like (year 2000 it's century year as well as leap year.)

"""
First, we check if the year is divisible by 4. If it is, it could be a leap year, but we need to consider further conditions.
If the year is divisible by 100, it might still be a leap year. However, if it is also divisible by 400, then it is a leap year. Otherwise, if it's only divisible by 100 but not by 400, it's not a leap year.
If the year is not divisible by 100, but it is divisible by 4, it is a leap year.
So, in Python, we express these conditions as follows:

year % 4 == 0: This checks if the year is divisible by 4.
year % 100 != 0: This ensures that if the year is divisible by 100, it is not considered a leap year unless it is also divisible by 400.
year % 400 == 0: This checks if the year is divisible by 400.
Combining these conditions using logical operators (and, or), we get the final expression to determine if a year is a leap year or not.
"""