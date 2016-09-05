
a=10

b=1.3

c=True

d="float"

e=(a,b)

f=[a,b,c,d]

g={e:f}


print a,b,c,d,e,f,g


print type(a)
print type(b)
print type(c)
print type(d)
print type(e)
print type(f)
print type(g)


print e[0]

print e[0:]


#e[0]=10

print f[:] 

print f[0:-1]


print f[-1:0:-1]

print d[:2]

print 1+3

print "a"+"b"


print "a"*3



print 6-4.5

print 6%4


print 3>2,5<=4,4!=4,3==5,4 in (3,4,5), [4] is [4], 5 is not 5


print [4]==[4]

ex=[5,[0,1]]

ex2=ex

import copy

ex3=copy.copy(ex)

ex4=copy.deepcopy(ex)

print "lalalala"
print ex is ex2,ex3 is ex,ex4 is ex


print ex,ex2,ex3,ex4
print ex3[1] is ex[1],ex4[1] is ex[1]

print True==1,False is 0,0 is 0


print False or True, True and False, 3 or False, False or 3,True and 4


print 3 or 5, 4 and 5 and 65

print not False

print not 3 

if not a:
    print "yes"
elif not b:
    print "no"
else:
    print "haha"
    print "nonono"



for i in ex:
    print i

i=10
while i>=3:
    
    i=i-1
    if i==7:
        print "noway"
        continue 
    else:
        if i==5:
            break
        pass

    print i

m=3
n=9

def func(a,b):
    if type(a)==int:
        a=a+b
        b=a*b
    else:
        a[0]=a[0]+b[0]
        b[1]=a[1]+b[1]
    print a,b
    return a,b

func(2,3)

func(3,3)

print func(m,n),m,n

mn=[0,3]

nm=[3,0]
print func(mn[0],mn[1]),mn[0],mn[1]

print func(mn,nm),mn,nm



class bird():
    weight=90

    def __init__(self,name,fly=40):
        self.name=name
        self.fly=fly or 0

    def flyheigh(self,miles):
        self.heigh=miles
        print self.heigh
        

monster=bird("monster",399)
coco=bird("coco",3)


print monster.weight,monster.name,monster.fly,monster.flyheigh(499)

print coco.weight,coco.fly


class creature(bird):
    def __init__(self,name,body):
        self.name=name
        self.body=body

    def run(self,speed):
        self.long=self.heigh*speed
        print self.long
    god="TUE"

human=creature("being","straight") 
print human.god,human.body,human.name,human.weight,human.flyheigh(10)
print human.heigh
print human.run(3),human.long

print creature.god
creature.god=10

print creature.god,human.god
human.god="sev"

print creature.god, human.god

print None,type(None)==None


print type("a")==str


print dir("a")
print dir(1)
print dir((3,))
print dir((4))


def argfunc(a,b,c,d=10,):
    print a,b,c,d

def sumfunc(*a,**d):
    print a,d,type(a),type(d)

def superfunc(**a):
    print a,type(a)

argdict1={"d":3}
arglist=(3,5,6)
argfunc(3,4,5,1)
argfunc(3,c=4,b=5)

print "hahahaahh"
sumfunc(1,*arglist,**(argdict1))
argfunc(*arglist)
sumfunc(2,3,4,5)
sumfunc(*arglist)

argdict={"a":3,"b":0,"c":5}
argfunc(**argdict)

superfunc(a=4,c=5,d=6)
superfunc(a=5,c=4,b=49,d=39)
argfunc(**argdict)




a=(1,3,4)
b=(3,4,56)
c=(3,2,5)

print zip(a,b,c)

e,f,g=zip(*zip(a,b,c))
print e,f,g


print range(0,10,2)


for i in enumerate(a):
    print i


with open("homework.txt") as files:
    """
    while True:
        if files:
            files.next()
            print files.next() 
        else:
            break
    for i in files:
        print i

    """
def genye():
    a=10
    yield a+10
    b=30
    yield b
    yield a+b


for i in genye():
    print i
    

G=(x for x in range(2,49,3))
tupe=(x for x in range(0))

lis=[x*2 for x in range(0,3)]


print G,type(G)
print tupe,type(tupe)
print lis,type(lis)
print dir(genye)

print genye.func_name





funlam=lambda x,y:x(3)*y

funex=lambda x:x*9

print funlam(funex,4)



mapfunc=map(funlam,[funex,funex,funex],[3,4,5])

print mapfunc

filterlist=filter((lambda x:x>4),[3,4,5,6])

print filterlist

reducelist=reduce((lambda x,y:x+y),range(1,100))

print reducelist

try:
    with open("homework.txt") as files:
        while True:
            if files:
                print files.next() 
            else:
                break
except StopIteration:
    print "roop finish"

finally:
    print "yeah i finish"

away=[2,4,5,5]

away[2]=None

del away[2]

print away



class updown():
    def __init__(self,name):
        self.name=name
    def __enter__(self):
        print "welcome"+self.name
    def __exit__(self,exc_type,exc_value,traceback):
        self.name="end"
        print "goodbye"+self.name

lucy=updown("lucy")

with lucy as lucy:
    pass
            
rudy=updown("rudy")
print rudy.__dict__,updown.__dict__



class propertytest(object):
    def __init__(self,weight):
        self.weight=weight
    def getvalue(self):
        return -self.weight
    def setvalue(self,value):
        self.weight=-value
    def delvalue(self):
        print "goodbye"
        del self.weight
    overweight=property(getvalue,setvalue,delvalue,"oper")

    def __getattr__(self,name):
        return name+" not found"

meimei=propertytest(30)

print meimei.weight,meimei.overweight

meimei.weight=499

print meimei.weight,meimei.overweight

meimei.overweight=29

print meimei.weight,meimei.overweight

#del meimei.weight

#print meimei.overweight

del meimei.overweight

#print meimei.weight

print meimei.good




def clo_ex():
    b=10
    def line(x):
        return x+b
    return line


cloone=clo_ex()

print b

print cloone(3)

print cloone(30)



def withpara(a,b):
    def line(x):
        return a*x+b
    return line


paraone=withpara(3,4)

paratwo=withpara(10,2)

print paraone(3),paratwo(4)


print paraone.__closure__

print paraone.__closure__[0].cell_contents

print paraone.__closure__[1].cell_contents



def decorator(f):
    def true_def(a,b):

        print "start"
        f(a,b) 
        print "end"

    return true_def

@decorator
def deal(a,b):
    print a,b


deal(2,3)


def dewithpara(para="hi"):

    def dewithparaone(f):

        def true_func(a,b):
            
            print para
            print "start"
            f(a,b)
            print "end"
        return true_func 

    return dewithparaone


@dewithpara("dada")
def sayhi(a,b):
    print a,b

sayhi("say","hi")


def decorate_class(f):
    class true_class:
        def __init__(self,name):
            self.weight=30
            self.oldclass=f("name")

        def rename(self,newname):
            print "confirm"
            self.oldclass.rename(newname)

    return true_class


@decorate_class
class baseclass():
    def __init__(self,name):
        self.name=name

    def rename(self,newname):
        self.name=newname
        print "success,your newname is "+self.name

product=baseclass("dong")

print product.oldclass,product.weight,product.rename("newworld")



num_a=1
num_b=1

print id(num_a),id(num_b),num_b is num_a


ab=["a",1]
dc=["a",1]


print id(ab),id(dc),ab is dc

acdddd=10000
ad="adb"

print id(acdddd),id(ad),acdddd is ad 


import sys

print sys.getrefcount(acdddd)

