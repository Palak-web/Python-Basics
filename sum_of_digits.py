num = int(input("Enter the num:"))
digits_int = []
for d in str(num):
    digits_int.append(int(d))
print(sum(digits_int))

# num_str = str(num)
# digits = [int(d) for d in num_str]
# print(sum(digits))