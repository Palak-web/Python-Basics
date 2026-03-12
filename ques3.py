"""Write a program that takes father's age and son's 
age as input from the user.
Find how many years ago OR in how many years 
the father was/will be exactly twice as old as son.

Example:
Input:  Dad=40, Son=15
Output: 10 years ago

Input:  Dad=30, Son=20
Output: 10 years later"""

def twice_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)

print(twice_old(40, 15))