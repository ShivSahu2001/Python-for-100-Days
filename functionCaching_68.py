from functools import lru_cache
import time

# It takes memeory
@lru_cache(maxsize=None)  #memoization
def fx(n):
    time.sleep(3)
    return n*10

print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(5))
print("Done for 5")

print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(5))
print("Done for 5")