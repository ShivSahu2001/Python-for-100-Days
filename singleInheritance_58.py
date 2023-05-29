class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species = "Dog")
#         self.breed = breed

#     def make_sound(self):
#         print("Bark!!")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Cat")
        self.breed = breed

    def cat_sound(self):
        print("Meow")


# d = Dog("Dog", "Doggy")
# d.make_sound()
c = Cat("Cat", "catty")
c.cat_sound()
a = Animal("Dog", "Dog")
a.make_sound()