class Person:
    name = "Raj"
    occupation = "SDET"
    netWorth = 10000
    # self point to current object
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
# a.name = "Shubham"
# a.occupation = "SDE"
# print(a.name)
# print(a.occupation)
a.info()