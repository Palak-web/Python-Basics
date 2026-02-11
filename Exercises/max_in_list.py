user = input("enter the list of num: ")
lst = user.split()
max = int(lst[0])
for com in lst:
    com = int(com)
    if com > max:
        max = com

print(f"{max} is greater num in list")
        