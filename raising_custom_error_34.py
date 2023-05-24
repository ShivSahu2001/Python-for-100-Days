a = input("Enter a value between 1 to 10: ")

if a == "quit":
    print("You quit the game!")
elif(int(a)<1 or int(a)>10):
    raise ValueError("Value should be between 1 to 10")

else:
    print(a)