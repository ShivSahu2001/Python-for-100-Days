
#Decorators are use to modify a function

def greet(fx):
    def myFx(*args, **kwargs):
        print("Hey Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return myFx

@greet
def hello():
    print("Hello World!!")

@greet
def add(a, b, c):
    print(a+b +c)

# greet(hello)()
# hello()
# greet(add)(1,2, 3)
add(1,2,3)