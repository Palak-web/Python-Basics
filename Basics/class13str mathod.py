#str are immutable 
a = 'Harry!!!Harry'
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry" , "bhooth"))
b= 'hello DoSton mera naam hai doremon'
print(b.capitalize())
#print(len(b))

g = "hello dear how are you"
print(g.center(50))
print(len(g))
print(a.count("Harry"))
str1 = "Welcome to the console !!!!"
print(str1.endswith("!!!"))
print(str1.endswith("the",5, 14))

str2 = "he's name is Dan, he is a goood man"
print(str2.find("is"))
print(str2.find("ishh"))
#print(str2.index("ishh")) it will give arror

str3="hellokdfkv222"
print(str3.isalnum())
print(str3.isalpha())

str4 = "hello world"
print(str4.islower())