class Employee:
    def __init__(self, name, id):
        self.name = name 
        self.id = id

    def showDetails(self):
        print(f"Employee Id is: {self.id} and Employee Name is: {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The Default Language is Python")

e = Employee("Bala", 20)
e.showDetails()

e2 = Programmer("Raj", 50)
e2.showDetails()
e2.showLanguage()