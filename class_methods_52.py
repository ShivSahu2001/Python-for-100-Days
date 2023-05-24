class Employee:
    company = "Apple"

    def showDetails(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    # By default here first argument is instance variable but after adding decorator @classmethod it will treat first argument as Class cls --> class variable
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Raj"
e1.showDetails()
e1.changeCompany("Google")
e1.showDetails()
print(Employee.company)