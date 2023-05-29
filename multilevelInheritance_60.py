class GrandMother:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Mother(GrandMother):
    def __init__(self, name, hobby):
        GrandMother.__init__(self, name, age = 56)
        self.hobby = hobby

    def show_Details(self):
        GrandMother.show_details(self)
        print(f"Hobby: {self.hobby}")

class Girl(Mother):
    def __init__(self, name, stream):
        Mother.__init__(self, name, hobby= "Cooking")
        self.stream = stream

    def show_Details(self):
        Mother.show_Details(self)
        print(f"Stream: {self.stream}")

gi = Mother("Sakshi", "Science")
gi.show_Details()

print(Girl.mro())
