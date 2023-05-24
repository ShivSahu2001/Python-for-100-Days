class Employee:
    def __init__(self, name , sal):
        self.name = name
        self.salary = sal

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0],int(string.split("-")[1]) )
    
   

e1 = Employee("Raj", 15000)
print(e1.name)
print(e1.salary)

string = "Bala-20000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls , string):
        name, age = string.split(",")
        return cls(name, int(age))

# string1 = 
p1 = Person.from_string("John, 23")
print(p1.name)
print(p1.age)
