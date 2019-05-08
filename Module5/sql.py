import sqlite3

conn=sqlite3.connect('anand.sqlite')
cur=conn.cursor()
#cur.execute('create table student(name text,usn INTEGER)')
cur.execute('insert into student(name,usn) values (?,?)',('anand',123))
cur.execute('insert into student(name,usn) values (?,?)',('kumar',456))
cur.execute('insert into student(name,usn) values (?,?)',('ramu',789))
cur.execute('select name,usn from student')
for x in cur:
	print(x)

cur.execute('select name,usn from student where usn>500')
for x in cur:
	print(x)
