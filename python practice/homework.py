# -*- coding: gbk -*-

import os,time,datetime,re
'''
year_=2004
month_=10
day_=1

if (year_%4==0 and year_%100!=0) or year_%400==0:
    print "%d是闰年"%year_
else:
    print "%d不是闰年"%year_


seconds_=datetime.datetime(2008,10,1)-datetime.datetime(1970,1,1)
print seconds_.total_seconds()
print time.localtime(seconds_.total_seconds()).tm_yday

'''
def read_file():
    global person_record,tag_name,need_update
    file_=file('record.txt','r')
    for line in file_:
        if len(line)>1:
            if line.startswith('#'):
                line=line.replace(' ','')
                tag_name=line
            else:
                line=line.replace(' ','')
                record=line.split(',')
                person_record.append(record)
    file_.close()

def find_person():
    score_less_60=[i[0] for i in person_record if int(i[2])<60]
    name_startswith_L=[i[0]for i in person_record if i[0].startswith('L')]
    sum_score=sum([int(i[2]) for i in person_record])

    print '得分少于60的人有：',score_less_60
    print '名字以L开头的人有：',name_startswith_L
    print '所有人的总分为：',sum_score

def update_file():
    global person_record,tag_name,need_update
    def capitalize(x):
        global need_update
        if not x[0].istitle():
            x[0]=x[0].capitalize()
            need_update=True
        return x
        
    person_record=map(capitalize,person_record)
    print person_record,need_update
    if need_update==True:
        print 'record.txt有人的名字不符合规定，需要更新'
        file_=file('record.txt','w')
        file_.write(tag_name)
        for record in person_record:
            file_.write(','.join(record))
        file_.close()
        print '更新完毕'
    else:
        print 'record.txt的人名字符合规定，不需要更新'


def re_filename():
    name='output_2000.12.1.txt'
    math_=re.search(r'output_(?P<year>\d{,4}).(?P<month>\d{,2}).(?P<day>\d{,2}).txt',name)
    timelist=map(lambda x:int(x),[math_.group('year'),math_.group('month'),math_.group('day')])
    datetime2=datetime.datetime(*timelist)
    seconds=datetime2-datetime.datetime(1970,1,1)
    time_struct=time.localtime(seconds.total_seconds())
    new_name=time.strftime('%Y-%m-%d-%w',time_struct)
    print new_name



if __name__=='__main__':
    tag_name=''
    person_record=[]
    need_update=False

    read_file()
    find_person()
    update_file()

    re_filename()
