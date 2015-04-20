class men(object):
    def __init__(self,age,height):
        self.age=age
        self.height=height
        self.dead=False

    def grown(self,year):
        self.age=self.age+year
        self.height=self.height+year*10

    def getChange(self):
        if self.dead==False:
            if self.age>=18:
                return 'adult'
            else:
                return 'kid'
        else:
            return 'this men is dead'
    def setChange(self,value):
        self.age=value
    def delChange(self):
        self.dead=True
        print 'delete'

    change=property(getChange,setChange,delChange,'a')
    

tony=men(1,20)
print tony.change
tony.change=32
print tony.age
print tony.change
del tony.change
print tony.dead
print tony.change
#print dir(tony)
tony.setChange(3)
print tony.age
'''
class num(object):
    def __init__(self, value):
        self.value = value
    def getNeg(self):
        return -self.value
    def setNeg(self, value):
        self.value = -value
    def delNeg(self):
        print("value also deleted")
        del self.value
    neg = property(getNeg, setNeg, delNeg, "I'm negative")

x = num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg
'''
