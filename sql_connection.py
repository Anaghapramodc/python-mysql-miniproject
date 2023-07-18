import mysql.connector

#mysql-python connecter
mydb=mysql.connector.connect(host='localhost',user='root',password='anagha123@A')
print(mydb)
mycursor=mydb.cursor()

#creat data base
# mycursor.execute("CREATE DATABASE Mydb_python")

#to display database
# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)

#to creat table in the data base
# mycursor.execute("use Mydb_python")
# mycursor.execute("create table test(name varchar(250),dept varchar(300),salary int);")

#to show table
# mycursor.execute("show tables")
# for x in mycursor:
#     print(x)

#to insert values in the table
mycursor.execute("use Mydb_python")
# sql="insert into test values ('jack','python',1234)"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")
# sql="insert into test values ('anagha','python',123456)"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

#to insert multiple values
# sql="insert into test(name,dept,salary) values(%s,%s,%s)"
# val=[
#     ('anagha','python',123456),
#     (' chitra','python',234567875),
#     ('neetha','python',3456)
#      ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,'records inserted')

#to print all values in the table
# s=str(input("enter the name"))
# mycursor.execute("select*from test")
# myresult=mycursor.fetchall()
# for x in myresult:
#     if s in x:
#         print("true")
#         break
#     else:
#         print("faulse")
#         break


#to print all values in  first row
# mycursor.execute("select * from test ")
# myresult=mycursor.fetchone()
# print(myresult)

#to print values in a specific row
# mycursor.execute("select * from test where name='neetha' ")
# myresult=mycursor.fetchone()
# print(myresult)

"""
relationship queries
1.one to one
eg=user-->password(one user with one password)
2.one to many
eg=one class--->multiple students(one class can have nultiple students)
3.many to many
eg=students--->
"""

#to delete specific values in a table
# sql="delete from test where name='chitra'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"records deleted")

#to update values in table
# sql="update test set salary='3456' where salary='1234'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"records updated")

#to sort the values
# sql="select * from test order by name"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
#
# for x in myresult:
#     print(x)
# #to sort the values in decenting order
# sql="select * from test order by name desc"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
#
# for x in myresult:
#     print(x)
#
# #to sort the values in asenting order
# sql="select * from test order by name asc"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
#
# for x in myresult:
#     print(x)

#to return distinct values
# sql="select distinct salary from test"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
#
# for x in myresult:
#     print(x)


#table1
# mycursor.execute("use Mydb_python")
# mycursor.execute("create table test1(name varchar(250),dept varchar(300),salary int);")

# mycursor.execute("show tables")
# for x in mycursor:
#     print(x)

# sql="insert into test1(name,dept,salary) values(%s,%s,%s)"
# val=[
#     ('akshaya','java',1236),
#      ('vishnu','sql',23875),
#      ('swetha','c++',345633)
#
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,'records inserted')
# # p=print("related works")
# x='jack'
# y='python'
# z='123'
# mycursor.execute("use Mydb_python")
# sql="insert into test(name,dept,salary) values(%s,%s,%s)"
# val=[
#     (x,y,z),
#      ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,'records inserted')

# mycursor.execute("use Mydb_python")
# sql="SELECT name,dept FROM test;"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# v="anagha"
# w="python"
# c=0
# for x in myresult:
#     print(x)
#     if x==(v,w):
#         c=c+1
#         print("present")
#
# if c==0:
#    print("not present")
#




# x="sanjusanjay23@gmail.com"
# mycursor.execute("use art_gallary")
# sql="select user_name from artist where gmail=x"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)
# for i in myresult:
#     for j in i:
#           print(j)









# mycursor.execute("use art_gallary")
# sql="select user_name from artist where gmail='sanjusanjay23@gmail.com';"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for i in myresult:
#     for j in i:
#           print(j)




# mycursor.execute("use art_gallary")
# mycursor.execute("select*from artist")
# myresult = mycursor.fetchall()
# print(myresult)
# d={1:'id_no',2:'user_name',3:'password',4:'painting_name',5:'mediam',6:'size',7:'price',8:'art_code',9:'contact_no',10:'gmail'}
# # print(l)
# dict={}
# t=0
# none = 1
# for i in myresult:
#     for x in i:
#         # print(x)
#         t=t+1
#         dict.setdefault(d.get(t),x)
#     print(dict)
#     dict={}
#     t=0

# d={"id":1,"name":"anagha","age":22,}
# x=d.get(id)
# print(x)
c=tuple('village')
print(type(c))
mycursor.execute("use art_gallary")
mycursor.execute("select*from artist_sell")
myresult = mycursor.fetchall()
# print(myresult)
d = {1: 'id_no', 2: 'gmail', 3: 'password', 4: 'painting_name', 5: 'mediam', 6: 'size', 7: 'price',8: 'art_code', 9: 'sell_or_not', 10: 'user_name'}
# print(l)
dict = {}
t = 0
for i in myresult:
   for x in i:
      # print(x)
      t = t + 1
      dict.setdefault(d.get(t), x)
   print(dict)
   if dict.get("painting_name")=='villege':
       c=dict.get('painting_name')
       mycursor.execute("use art_gallary")
       sql = "update  artist_sell set sell_or_not='NOT SELL' WHERE painting_name="+"'"+c+"'"
       # sql="update test set salary='3456' where salary='1234'"
       mycursor.execute(sql)
       mydb.commit()
       print(mycursor.rowcount,"records updated")
   dict = {}
   t = 0




