tup = (1,5,"book",6)
print(type(tup))

tup = (1)
print(type(tup))
#so if you print a single value it will take it as a int, So for type of tuple a comma is necessary

tup = (1,)
print(type(tup))

'''tupe = (1,4)
tupe[0] = 8
print(tupe)'''
#TypeError: 'tuple' object does not support item assignment so tuple are immutable you can not change the value which is pre- defined

tupe = [6,7,8,9]
tupe[2] = 11
print(type(tupe))# lists are mutable

tup =(2,4,6,5,"hey", "ram", 4 ,0)
if 4 in tup:
    print("yes it is present in tup")

tup2 = tup[0:7:2]
print(tup2)