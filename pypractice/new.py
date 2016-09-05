print "hello"
print type('a')==str
print type("a")
tuplea = {"1":[3,5],"a":("a",2),1:"d"}
print tuplea["a"]
print tuplea["1"]
print tuplea[1]

print tuplea["a"][1]


print "adfbex"[5:]
class specialattr():
	def __init__(self,value):
		self.value=value
	def Getop(self):
		return -self.value
	def Setop(self,value):
		self.value=-value
	def Delop(self):
		print("del value")
		del self.value		
	opvalue=property(Getop,Setop,Delop,"property attr")

newattr=specialattr(30)
print newattr.opvalue
newattr.opvalue=-30
print newattr.opvalue,newattr.value
del newattr.opvalue
print newattr.value,newattr.opvalue


"""
def closure_f(a,b):
	def clo_re(x):
		print a*x+b
	return clo_re

new_clo_a=closure_f(2,1)
new_clo_b=closure_f(4,3)

new_clo_a(2)
new_clo_b(2)


def decorator_q(word):
	def de_inside(func):
		def new_f(a,b):
			print word
			func(a,b)
		return new_f
	return de_inside


@decorator_q("haha")
def calculate(a,b):
	print a+b

@decorator_q("yeye")
def calulate(a,b):
	print a*b

calculate(3,3)
calulate(3,3)


class bird(object):
	name="bird"
	pos=0
	def __init__(self,spname,moveway):
		self.spname=spname
		self.moveway=moveway
		print "new bird birth:%s"%spname
	def move(self):
		if self.moveway=="walk":
			self.pos=self.pos+1
		else:
			self.pos=self.pos+10
	def getneg(self):
		return -self.pos

	def setneg(self,value):
		self.pos=-value
	def delneg(self):
		del self.pos

	negpos=property(getneg,setneg,delneg)

bird1=bird("maque","walk")
bird2=bird("xiaoji","fly")

bird1.move()
bird2.move()

print bird1.pos,bird2.pos
print 1 or 0

print "start"
print bird1.negpos
bird1.negpos=10
print bird1.negpos,bird1.pos

del bird1.negpos

print bird1.negpos,bird1.pos

print "END"

class creature(bird):
	category=1
	def eatable(self):
		if self.category==1:
			print True

human=creature("man","walk")
human.eatable()
human.move()
print human.pos



def can(a=1,*c,**d):
	print a,c,d

can(3,4,5,6,b="q")

can(3,*[1,2],**{"b":"q"})




for i in range(0,100,10):
	print i


for a,b in enumerate((1,3,40)):
	print a,b

for i in zip((1,3,4),["a","0","d"]):
	print i

a=[1,2,3]
b=[4,5,6]

c=[x+y for x,y in zip(a,b) if x>=2]

print c



name= lambda x,y:x-y

print name(2,4)


a="abcdefg"

print map(lambda x:x.upper(),a)

def filterfunc(x):
	if ord(x)>99:
		print ord(x)
		return x
	else:
		return False

print filter(filterfunc,a)

reducefunc=lambda x,y:'-'.join((x,y))

print reduce(reducefunc,a)

try:
	for i in range(0,10):
		print i[0]

except:
	print "loop done"

else:
	print "no except"

finally:
	print "thanks for watching"

class fakelist(list):
	def __init__(self,arg):
		if type(arg)!= iter:
			list(arg)
		else:
			print "arg must be iterable"


class superlist(list):
	def __sub__(self,subobj):
		a=self[:]
		b=subobj[:]
		print a,b
		return True
noknown=superlist([2,4])
print noknown	
print superlist([1,2,4])-superlist([3,0,-1])


class superList(list):
    def __sub__(self, b):
        a = self[:]    
        b = b[:]        
        print a,b
	while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print superList([1,2,3]) - superList([3,4])



"""

