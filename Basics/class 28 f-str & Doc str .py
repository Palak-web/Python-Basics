letter = "Hey my name is {} and I am from {}"
country = "India"
name ="Harry"

#print(letter.format(name,country))
# to yha values aage piche ho saki hain to iske liye hum f - string ka use karne hai

print(f"Hey my name is {name} and I am from {country}")
price = 4.099999
txt =f"For only {price:.3f}dollar"
print (txt)

def square(n):  #aur ye docstr function ke just next line me hona chahiye nhi to none dikhayega
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)
