city = ("Barabanki", "lko","jaypur", "Gonda", "Gorakhpur")
city2 = list(city)
city2[1] = "delhi"  #change item
print(city2)
city2.pop(2)    #remove item
print(city2)
city2.append("lucknow")  #add item
print(city2)
city2 = tuple(city)
print(type(city))

tuple = (1,2,3,2,31,1,3,2,3)
# res = tuple.count(3)
# res = tuple.index(3)
# res = tuple.index(311)
# res = tuple.index(3,4,8)
res = len(tuple)
print("Count of 3 in tuple is: ", res)