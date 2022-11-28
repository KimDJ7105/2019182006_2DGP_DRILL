class NPC :
    def __init__ (self,name, _x, _y):
        self.name, self.x, self.y = name, _x, _y

yuri = NPC("Yuri",100,100)
yuri.__dict__['age'] = 30
print(yuri.__dict__)
print(yuri.age)

tom = NPC("Tom",100,200)
print(tom.__dict__)