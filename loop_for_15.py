# name = "Shiva"

# for i in name:
#     print(i)
#     if(i == "h"):
#         print("take a pause")

# colors = ["green", "blue","red"]
# for color in colors:
#     print(color)
#     for col in color:
#         print(col)

# here 5 is exclusive
# for k in range(5):
#     print(k)

# for k in range(1,11):
#     print(k)

# range(start, end-1, gap or jump)
# for k in range(1,21,3):
#     print(k)

number = int(input("Enter a number for a table: "))
for tab in range(1,11):
    print(number * tab)