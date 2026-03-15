marks =[ 3,5 , 7, "palak" , 10]
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[-3])# negative index rule(length - the value = index value)
#[5-3 = 2 means 7]
# list in mutable but tuple is not immutable

if 3 in marks:
    print("yes")

#same thing you can do with string
if "pal" in marks:
    print("yes")

if "palak" in marks:
    print("yes")

print(marks)
print (marks[1:4:2])


lst = [i for i in range(4)]
print(lst)


l =[ 4,8,1,3,2,7,5,7,7,6]
l.append(9)
print(l)
l.sort(reverse=True)
print(l)
print(l.index(3))
print(l.count(7))
m = l.copy()
m[0] = 0
print(l)
print(m)
l.insert(1,999)#ab yha list me 999 ki index value 1 hogi
print(l)
m = [555 ,666,90]
l.extend(m)
print(l)