class Calci(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b

obj = Calci(a=10, b=20)
print(obj.add(), obj.subtract())
