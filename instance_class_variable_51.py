class Employee:
    # Class Variable --> sabke liye same honge
    companyName = "Google"
    numOfEmployees = 0
    def __init__(self, name):
        # Instance variable --> hara ak object ke liye change honge
        self.name = name
        self.age = 18
        Employee.numOfEmployees += 1
    def showDetails(self):
        print(f"The name of the employee is {self.name} and age is {self.age} works in {self.companyName} and the size of company is {self.numOfEmployees}")

e = Employee("Raja")
# First of variable is searched in Instance variable if not found we take the class variable
# But in this we found in Instance varaible s so we don't take the class variable
e.companyName = "Microsoft"
print(Employee.companyName)
e.showDetails()
e1 = Employee("Shyam")
e1.age = 22
e1.showDetails()


# Employee.showDetails(e)
