
def my_generator():
    for i in range(5):
        # complex computation
        yield i # yield is used then it is using generators

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)