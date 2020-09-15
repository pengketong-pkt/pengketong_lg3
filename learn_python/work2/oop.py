class person:
    def __init__(self,shengao,tizhong,name):
        self.shengao = shengao
        self.tizhong = tizhong
        self.name = name

    def saodi(self, name):
        print("扫地")
    def yundong(self, name):
        print("运动")


p1=person(1.5,100,"zhangsan")
print(p1.shengao)
print(p1.tizhong)
print(p1.name)
p1.saodi("zhangsan")