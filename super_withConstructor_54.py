class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

raj = Employee("Raj Shah", 123)
janvi = Programmer("Janvi Shah", 12345, "Python")

print(janvi.name)
print(janvi.id)
print(janvi.lang)