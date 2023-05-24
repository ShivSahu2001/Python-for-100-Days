# for i in range(11):
#     if(i==10):
#         break
#     print("10 x", i+1, "=", 10 * (i+1))

# print("come out of the loop")

# for i in range(12):
#     if(i==10):
#         print("Skip the iteration")
#         continue
#     print("10 x", i+1, "=", 10 * (i+1))

# continue --> skips the iteration
for i in [2,4,5,6,7,8]:
    if(i%2 != 0):
        continue
    print(i)