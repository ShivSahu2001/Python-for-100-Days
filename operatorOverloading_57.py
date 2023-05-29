class Vector:
    def __init__(self, i, j , k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, a):
        return Vector(self.i + a.i , self.j + a.j , self.k + a.k)
        

v1 = Vector(3, 4, 5)
print(v1)
v2 = Vector(5, 6, 7)
print(v2)



print(v1 + v2)
print(type(v1 + v2))