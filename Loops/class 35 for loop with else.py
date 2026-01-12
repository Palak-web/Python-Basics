for i in range(5):
    print(i)
else:
    print("Sorry no i")

#yha else ke execute hone ka matlab hi hai ki loop break nhi hua loop khatam hua hai
#and uske baad else part execute hota hai

for i in range(5):
    print(i)
    if i ==4:
        break
else:
    print("Sorry no i")

# and same thing happens with while loop
i = 0
while i<7:
    i = i + 1
    print(i)
    # if i ==5:
    #     break

else:
    print("Sorry no i")