def average(a = 9 , b = 1):
    print("The avg is ", (a+b)/2)


average(4,5)

def average(*numbers):
    print(type(numbers))
    for i in numbers:
        sum = i +1
        print("average"    , sum/len(numbers))
average( 5 , 7)