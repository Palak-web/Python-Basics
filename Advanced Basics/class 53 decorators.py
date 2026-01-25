def greet(fx):

    def mfx(*args, **kargs):
        print("Good Morning")
        fx(*args, **kargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello Palak")

# @greet
def add(a ,b ):
    print(a+b)

hello() #or greet(hello())
greet(add)(6,1)