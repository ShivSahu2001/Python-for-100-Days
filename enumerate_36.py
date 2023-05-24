marks = [34, 23, 67, 85, 98, 25]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print(" The Shiv is Great!!")
#     index += 1

for index,mark in enumerate(marks, start=1):
    print(index,  mark)
    if(index == 3):
        print("The Shiv is Great!!")

