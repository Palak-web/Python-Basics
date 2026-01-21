#Function to double the input
# def double(x):
#     return x * 2
# print(double(4))

# #Lambda function to double the input
double = lambda x: x * 2
cube = lambda x: x*x*x
avg = lambda x,y,z:(x+y+z)/3

print(avg(4, 3, 5))
print(cube(3))
print(double(4))

