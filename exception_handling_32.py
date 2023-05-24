num = input("Enter a number: ")
print(f"Multiplication table of {num} is: ")

try:
    for i in range(1, 11):
        print(f"{num} x {i} = {int(num)*i}")
except:
    print("Invalid Input!!")

print("Some imp lines of code")
print("End of program")


