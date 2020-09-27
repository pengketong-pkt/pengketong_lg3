class Person:
    def __init__(self, shengao, tizhong, name):
        self.shengao = shengao
        self.tizhong = tizhong
        self.name = name

    def saodi(self, name):
        print("扫地")

    def yundong(self, name):
        print("运动")


class Pen:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def write(self):
        print("写字")


p1 = Person(1.5, 100, "zhangsan")
print(p1.shengao)
print(p1.tizhong)
print(p1.name)
p1.saodi("zhangsan")

Pen1 = Pen("铅笔", "黑色")
print(Pen1.colour)
print(Pen1.name)
Pen1.write()
