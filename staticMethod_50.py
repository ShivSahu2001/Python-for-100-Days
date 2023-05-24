class Math:
    def __init__(self, num):
        self.num = num

    def addToNum(self, n):
        self.num = self.num + n

    # In static method we don't give self as a parameter
    @staticmethod
    def add(a, b):
        return a + b

m = Math(5)
print(m.num)
m.addToNum(5)
print(m.num)
# Static methods are not associated with instances and methods
# print(m.add(10, 20))
print(Math.add(10, 20))