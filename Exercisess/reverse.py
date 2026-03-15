a = (input("Enter your word/num:"))
if a.startswith("-"):
    val = a[:0:-1]
    print("-"+val)
else:
    print(a[::-1])
    