a = [1,2,43] #List are mutable
b = [1,2,43]

print(a is b) #exact location of object in memory
print(a == b) #it compares the value

a = 3 # it is immutable 
b = 3 #memory location me ye ek baar save ho jata hai 

print(a is b) #exact location of object in memory
print(a == b) #it compares the value

a = "Python" # it is immutable 
b = "Python" #memory location me ye ek baar save ho jata hai 

print(a is b) #exact location of object in memory
print(a == b) #it compares the value

a = None # it is immutable 
b = None #memory location me ye ek baar save ho jata hai 

print(a is b) #exact location of object in memory
print(a is None )
print(a == b) #it compares the value

#SO 'is' OPERATOR COMPARES THE IDENTITY 
# AND '==' OPERATOR COMPARES THE VALUE 