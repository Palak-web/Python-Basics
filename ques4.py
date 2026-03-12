"""Write a function that takes an array of numbers and returns the sum of the numbers.
 The numbers can be negative.
 If the array is empty, return 0."""
def sum_array(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_array([1, 2, 3]))