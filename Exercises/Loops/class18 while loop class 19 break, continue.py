#i = 3
#while(i<11):
#    print(i)
#    i = i+1


i = 6
while(i>0):
    print(i)
    i = i -1
else:
    print("Now i am outside the loop")


i = 0
for i in range(12):
    if(i==10):
      print("Skip the iteration")
      break
    print("5 X ",i+1 , "=" ,5*(i +1))

i = 0
for i in range(12):
    if(i==10):
      print("Skip the iteration")
      continue
    print("5 X ",i+1 , "=" ,5*(i +1))


