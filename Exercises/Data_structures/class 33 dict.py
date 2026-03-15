dict = {
    "Harry": "Human being",
    "spoon": "Object",
    100: "Subh",
    101: "Neha",
    102: "Ravi",
    103: "Palak Queen"
}
print(dict["Harry"])

info = {"name": "Ravi", "age": 19, "class": "BBA"}
print(info)
#they both printing same value if it is exsisting in the dict 
print(info["name2"])  # but if given variable does not exsist than it will give error 
print(info.get('name2')) #but it will give none
print(info.keys())
print(info.values())

for key in info.keys():
   print(info[key])

print(info.items())

for key in info.keys():
    print(f"The value corresponding to {key} is {info[key]}")