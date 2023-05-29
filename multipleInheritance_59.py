class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The Dance is {self.dance}")

class DancerEmployee( Employee,  Dancer):
    def __init__(self, dance ,name):
        self.dance = dance
        self.name = name

dE = DancerEmployee("Odisi", "Riya")
print(dE.name)
print(dE.dance)
dE.show()
print(DancerEmployee.mro())