year = int(input("Enter The year: "))
if (year % 400 == 0) or (year % 4== 0 and year % 100 != 0):
    print("Leap Year - 366 days")
else:
    print("not leap year -365 days")