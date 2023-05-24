
# marks = (49, 54, 87, 94, 37)

# temp = list(marks)
# temp.append(70)
# temp.pop(3)
# temp[1] = 84
# marks = tuple(temp)
# print(marks)

marks1 = (32, 45, 65)
marks2 = (87, 65, 97)

marks3 = marks1 + marks2
print(marks3)

# res = marks3.count(65)

# first argument is what you want to find and next two arguments are slice part
res = marks3.index(65, 3, 5)
print(res)
# print("Count of 65 in the tuple is: ", res)