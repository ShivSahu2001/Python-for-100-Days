fruit = "Orange"
print(len(fruit))
print(fruit[0:5]) # including 0 but not 5
print(fruit[1:5]) #including 1 but not 5
print(fruit[:5])
print(fruit[:])
# print(fruit[0:len(fruit)-3])
print(fruit[0:-3])

# 5:2 --> does not print anything
print(fruit[-1:-4])

# 2:4
print(fruit[-4:-2])

#Quick Quiz:
nm = "Shiv"
print(nm[-4:-2])
# 0:2