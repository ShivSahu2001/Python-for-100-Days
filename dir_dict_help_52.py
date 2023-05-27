# x = [1, 2, 3]
# print(dir(x))
# print(x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = "A"

p = Person("Raj", 45)
print(p.__dict__) # will give the result in dictinoary form

print(help(Person))