marks = [3,6,8,"raj", 56, True]
# print(marks)
# print(marks[0])
# print(marks[1])

# print(marks[-3])

# if "raj" in marks:
#     print("Yes")
# else:
#     print("No")

#same thing applies for strings as well

# if "ra" in "raj":
#     print("Yes")

print(marks)
print(marks[:])
print(marks[1:-2])

# 1:4 slice of list and 2 --> jump or gap 
print(marks[1:4:2])

# List Comprehension
lst = [i for i in range(10)]
print(lst)
lst = [i*i for i in range(11)]
print(lst[1:])

lst2 = [i*i for i in range(11) if(i%2==1)]
print(lst2)

names = ["raj", "Bala", "Rohit", "Piyush", "Omkar"]
namesWith_a = [item for item in names if "a" in item ]
print(namesWith_a)



