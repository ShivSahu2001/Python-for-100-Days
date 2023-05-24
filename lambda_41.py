# def double(x):
#     return x*2

# Higher order function
def apply(fx, value):
    return 10 + fx(value)

# For making one liner function we use Lambda Function
double = lambda x: x*2
cube = lambda x: x*x*x
avg  = lambda x,y,z: (x+y+z)/3

print(double(5))
print(cube(5))
print(avg(3,4,5))
print(apply(lambda x: x*x*x, 3))