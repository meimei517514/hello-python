# -*- coding: gbk -*-

import os,time,datetime,re

def jugle_time():
    year_=2004
    month_=10
    day_=1

    if (year_%4==0 and year_%100!=0) or year_%400==0:
        print "%d是闰年"%year_
    else:
        print "%d不是闰年"%year_

    print '2008.10.1是一年中的第%d天'%datetime.datetime(2008,10,1).timetuple().tm_yday


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
    datetime_real=datetime.datetime(*timelist)
    datetime_str=datetime_real.strftime('%Y.%m.%d')
    print "文件改名后为%s.txt"%datetime_str



if __name__=='__main__':
    tag_name=''
    person_record=[]
    need_update=False

    jugle_time()
    read_file()
    find_person()
    update_file()

    re_filename()
