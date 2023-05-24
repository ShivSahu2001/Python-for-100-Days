
# Reading a File
# f = open("myfile2.txt", 'r')


# text = f.read()
# print(text)
# f.close()

# Writing a File
# f = open("myfile2.txt", 'a')
# f.write("Hello World!, added")
# f.close()

# with open("myfile2.txt", 'a') as f:
#     f.write("Hey I am inside with")

# f = open('multiLine.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     # print(line)
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])

#     print(f"Marks of student {i} in Maths is: {m1*2}")
#     print(f"Marks of student {i} in Science is: {m2*2}")
#     print(f"Marks of student {i} in Hindi is: {m3*2}")

#     print(line)


f = open("writeMultiLine.txt",'w')
liners = ['line1', 'line2','line3','line4' ]

for line in liners:
    f.write(line + "\n")
f.close()