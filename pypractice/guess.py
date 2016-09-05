#i -*- coding: cp936 -*-
import random,time,copy,itertools,collections

def random_num():
    num_list= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    random_number=''.join(random.sample(num_list,4))
    return random_number

def get_posible_serial():
    num_list= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    all_posible_obj=itertools.permutations(num_list,4)
    all_posible_serial=map(lambda x:''.join(x),list(all_posible_obj))
    return all_posible_serial
    
def men_guess_number():
    while True:
        guess_number=raw_input("your turn:")
        if not guess_number.isdigit():
            print("not number,plaese enter again")
        elif len(guess_number)!=4:
            print("len must be 4,please enter again")
        else:
            repeat_num=max(collections.Counter(guess_number).values())
            if repeat_num>1:
                print ("repeat number,please enter again")
            else:
                break
    return guess_number

def check(guess_number,random_number):
    a_num=len(filter(lambda x:guess_number.index(x)==random_number.index(x),set(guess_number)&set(random_number)))
    b_num=len(filter(lambda x:guess_number.index(x)!=random_number.index(x),set(guess_number)&set(random_number)))
    return "%sA%sB"%(a_num,b_num)
            
def calculate(men_guess,result,old_posible_serial):
    right_a=int(result[0])
    right_b=int(result[2])
    iter_serial=copy.deepcopy(old_posible_serial)
    for serial in iter_serial:
        if len(set(men_guess)&set(serial))!=right_a+right_b:
            old_posible_serial.remove(serial)
        else:
            righta_num=len(filter(lambda x:men_guess.index(x)==serial.index(x),set(men_guess)&set(serial)))
            if righta_num>right_a:
                old_posible_serial.remove(serial)
    return old_posible_serial

class guess():
    def __init__(self,identity):
        if identity=='men':
            self.guess=men_guess_number()
            self.result=check(self.guess,random_number)
            self.right="Congratulations!You win!"
            self.wrong="Incorrect!you result is:%s"%self.result
        else:
            self.guess=random.choice(all_posible_serial)
            self.result=check(self.guess,random_number)
            self.right="Haha i win.Hail HYDRA!"
            self.wrong="No,it can't be!my result is:%s"%self.result
    
    def guess_check(self):
        if self.result[0]=='4':
            print self.right
            return True
        else:
            print self.wrong
            
if __name__=="__main__":
    all_posible_serial=get_posible_serial()
    random_number=random_num()
    print "Let's begin!!!"
    while True:
       men=guess('men')
       if men.guess_check():
           break
        
       calculate(men.guess,men.result,all_posible_serial) 
       pc=guess('pc')
       time.sleep(0.5)
       print 'My turn:',pc.guess
       calculate(pc.guess,pc.result,all_posible_serial)
       if pc.guess_check():
           break

