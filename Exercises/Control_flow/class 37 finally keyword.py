def func1():
    try:
        l = [1,2,5,7,9]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I'm always executed")
    # print("I am always executed")

x = func1()
print(x)
#so finally ka main use hota hai jab hum koi function banate hain to vo return ho ya na ho finally part execute hota hi hota hai
#but normal simply print return nhi hota hai 