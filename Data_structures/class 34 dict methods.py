ep1 = {100: 45, 101: 50, 102: 44, 103:40}
ep2 = {200: 50 ,201: 49, 202: 39}

ep1.update(ep2)
print(ep1)
#dict is a ordered DS
ep1.pop(102)
print(ep1)
ep1.clear()
print(ep1)
ep1.popitem()
print(ep1)
del ep1
print(ep1)
