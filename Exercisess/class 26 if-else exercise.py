import time
timestamp =time.strftime('%H:%M:%S')
print(timestamp)

hour=int(time.strftime('%H'))

if(hour<12):
    print("Good morning sir")

elif(hour >= 12 and hour <= 16):
    print("Good afternoon sir")

else:
    print("good evning Sir")
print("How are you sir")
#I did it..... buuurrrhhhh