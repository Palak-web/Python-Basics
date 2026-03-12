# Decorator function
def greet(fx):
    
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

# Function to be decorated
@greet
def hello():
    print("Hello world")

# Another normal function
def add(a, b):
    print(a + b)

# Calling the decorated function
hello()



def run(fx):

    def mfx(*args, **kargs):
        print("You Number is")
        fx(*args, **kargs)
        print("This is your answer")
    return mfx

@run
def positive(a, b):
    print(a + b)

positive(5, 6)