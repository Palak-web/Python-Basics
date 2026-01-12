s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1 , s2)

cities = {"Tokyo","Delhi", "Lucknow","Seoul","Madrid", "Kabul"}
cities2 = {"Tokyo", "Madrid", "Barabanki","Berlin"}
cities3 = cities.union(cities2)
cities3 = cities.union(cities2)
cities3 = cities.symmetric_difference(cities2)
print(cities3)
cities.intersection_update(cities2)
print(cities)
print(cities.isdisjoint(cities2))
print(cities.issuperset(cities2))
cities.remove("Tokyo")
print(cities)
(cities.discard("Tokyo2"))
print(cities)
item = cities.pop()
print(cities)
print(item)
del cities
print(cities)
cities.clear()
print(cities)
print(cities.issubset(cities2))

info = {"Carla",3,4343,"Happy", False}
if "Carla" in info:
    print("Carla is present in info")
else:
    print("Carla is absent")