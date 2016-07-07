import sqlite3

db_name="sqlite3test.db"


db_data=sqlite3.connect(db_name)

print "connect db success"


db_data.execute("DROP TABLE IF EXISTS human")  

db_data.execute("CREATE TABLE human (id int primary key not null,name string not null,sex string not null,age int not null)")

print "create table human done"


db_data.execute('''INSERT INTO human (id,name,sex,age) values(1,"Pony","man",28)''')

print "insert new data to human"


data=db_data.execute('''SELECT * FROM human''')


for i in data:
	print i


db_data.execute('''UPDATE human SET name="meimei" where id=1''')

print "update human name"

data=db_data.execute('''select name from human where id=1''')

print list(data)


db_data.execute('''delete from human where id=1''')

db_data.execute('''insert into human (id,name,sex,age) values(2,"meimei","woman",26)''')

db_data.commit()

db_data.close()

print "close db"
