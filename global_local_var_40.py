myName = "Shiv"
num = 10
print(myName)
print(num)
def greetingMyName():
    global num # you can change the global variable using this syntax but it is not a good practice
    num = 5
    myName = "Raj"
    print(f"Good Morning {myName}")

greetingMyName()

print(f"Good Morning {myName}")
print(num)