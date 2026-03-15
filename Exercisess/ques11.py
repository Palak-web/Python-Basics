"""Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

Example: (Input1, Input2 -->Output)
"4",  "5" --> "9"

Notes:
* If either input is an empty string, consider it as zero.
* Inputs and the expected output will never exceed the signed 32-bit integer limit (`2^31 - 1`)"""

def sum_strings(a, b):
    
    num1 = 0 if a == "" else int(a)
    num2 = 0 if b == "" else int(b)
    return str(num1 + num2)

result1 = sum_strings("4", "5") 
result2 = sum_strings("", "") 
result3 = sum_strings("-5", "3")
result4 = sum_strings("2", "")
print(result1)
print(result2)
print(result3)
print(result4)
print(type(result1))
