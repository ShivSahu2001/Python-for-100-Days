
class Person:

    # constructors automatically calls when an object is created
    # self is automatically passed
    def __init__(self, n, o):
        print("Hey I am a Person!!")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Raj", "SDET")
b = Person("Piyush", "Designer")
c = Person(1, 2)
a.info()
b.info()
c.info()