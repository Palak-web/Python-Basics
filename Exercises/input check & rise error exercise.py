a = input("Enter any value: ")
# check: agar input exactly "quit" hai to pass otherwise try me check karega
if (a == "quit"):
    pass
else:
    try:
        num = int(a)
        if 5<num or 9>num:
            pass
        else:
            raise ValueError("Number is not between 5 to 9")
            #agar no. 5 to 9 ke beech nhi hua to ye error 
    except:
        raise  ValueError("value error")
        # if try condition fail ho gyi to(QUIT,1b5, abc,etc.) to ye error