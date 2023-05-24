# class Employee:
    # def __init__(self):
        # Here name is public
        # self.name = "Raj"

        # here name is private because we have add __ as prefix
        # self.__name = "Raj"


# a = Employee()
# print(a.name)
# Cannot be access directly
# print(a.__name)

# Here __name is known as Name Mangling 
# print(a._Employee__name) # Can be accessed Indirectly

# Show all the methods in a 
# print(a.__dir__())

# Protected Access Specifiers

class Student:
    def __init__(self):
        self._name = "Bala"

    # Protected Method
    def _funName(self):
        return "The Python Class"
    
class Subject(Student):
    pass


obj = Student()
obj1 = Subject()
print(dir(obj))

# Calling by object of Student class
print(obj._name)
print(obj._funName())

# Calling by object of Subject class
print(obj1._name)
print(obj1._funName())