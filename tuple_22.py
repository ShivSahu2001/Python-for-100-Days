# Tuples are immutable

tup = (23, 43, 54, 67, 97, "raj", True)
# tup[1] = 34 --> not supported
print(tup, type(tup))

print(tup[0])
print(tup[-2])

if "raj" in tup:
    print("Yes")
else:
    print("No")

tup2 = tup[1:5]
print(tup2[1:5])

# last arguement is jump or gap
print(tup2[1:5:2])
