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