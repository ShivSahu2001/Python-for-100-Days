
import time

# def usingFor():
#     for i in range(5000):
#         print(i)

# def usingWhile():
#     i = 0
#     while i < 5000:
#         i = i+1
#         print(i)

# init = time.time()
# usingFor()
# t1 = time.time() - init
# init = time.time()
# usingWhile()
# print(time.time() - init)
# print(t1)


# print(5)
# time.sleep(3)
# print("Print after 3 seconds")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)