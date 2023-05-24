# Strings are immutable

nm = "!!!!Shiv!!!! !!!!!!Shiv"
print(len(nm))
print(nm.upper())
print(nm.lower())
print(nm.rstrip("!"))
print(nm.lstrip("!"))
print(nm.replace("Shiv", "Shiva"))
print(nm.split(" "))
title = "intro tO pYthon"
print(title.capitalize())

str1 = "Hey There Everyone!"
print(len(str1))
print(len(str1.center(50)))
print(str1.center(50))

print(nm.count("Shiv"))

myIntro = "Hey There Everyone!"
print(myIntro.endswith("Everyone!"))

str1 = "Welcome to the conole!!!"
print(str1.endswith("to",4,10))

str1 = "He's name is raj. He is great"
print(str1.find("is"))
# index is same as find() but it is more strict than find()
# print(str1.index("isfigj"))

str1 = "HiiThere"
print(str1.isalnum())

str1 = "HiiThere00"
print(str1.isalpha())

print(str1.islower())

str1 = "Hey EveryOne \n"
print(str1.isprintable())

str2 = "    "
print(str2.isspace())

str1 = "hey There everyone"
print(str1.istitle())

print(str1.isupper())

print(str1.startswith("hey"))

str1 = "hey There Everyone"
print(str1.swapcase())

print(str1.title())

