"""
Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
Write a code that gives out the total amount for different days(d)."""
def rental_car_cost(d):
    if d >= 7:
        res = d * 40 - 50
        return res
    elif 3 <= d < 7:
        res = d * 40 - 20
        return res
    else:
        res = d * 40
        return res

print(rental_car_cost(7))
print(rental_car_cost(3))
print(rental_car_cost(1))