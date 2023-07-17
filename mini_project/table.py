import mysql.connector

# mysql-python connecter
mydb=mysql.connector.connect(host='localhost',user='root',password='anagha123@A')
print(mydb)
mycursor=mydb.cursor()
#creat data base
# mycursor.execute("CREATE DATABASE art_gallary")
"""

table-artist

"""
#to creat table in the data base
# mycursor.execute("use art_gallary")
# mycursor.execute("create table artist(id_no int,user_name varchar(300),password varchar(300),painting_name varchar(300),mediam varchar(300),size varchar(300),price int,art_code varchar(300),contact_no int,gmail varchar(300));")

#to insert values in the table
mycursor.execute("use art_gallary")
# sql="insert into artist values (1,'sanjay','sanju123@','Abstract','acrylic on canvas','36*59 inches',165000,'DD08',7045025310,'sanjusanjay23@gmail.com')"
# sql="insert into artist values (2,'shamendu sonavane','shammu@172','Seascape','acrylic on canvas','16*16 inches',450000,'EE09','6238420162','shamendu12@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")
# sql="insert into artist values (3,'Rajan Raghavan','rajan@142','Abstract','acrylic on canvas','8*8 inches',554250,'QW78','8802437214','rajrajan12@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")
# sql="insert into artist values (4,'ganapati hegda','ganapathi12@','Ganesha','Oil on canvas','24*24inches',4100000,'TR76','9874302243','ganapathi34@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")
# sql="insert into artist values (5,'Punekar','punness21@','Tantric abstract','acrylic on canvas','36*36 inches',5420100,'GG45','8864534531','punekae99@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

# sql="insert into artist values (6,'sanjay chakrabarty','sanju09@','reflection','acrylic on canvas','13*14 inches',63200,'FH66','9962510234','sanjusanju@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

# sql="insert into artist values (7,'Dipti kumar','dipti88@','maharaas','Oil on canvas','24*24 inches',452000,'AD33','6254120321','dipti66@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

# sql="insert into artist values (8,'ghanshyam gupta','ghan23@','meditation','acrylic on canvas','8*8 inches',54200,'AQ23','9965021304','ghanshyam44@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

# sql="insert into artist values (9,'ghanshyam nayak','ghan23@32','villege','acrylic on canvas','8*8 inches',4320000,'AS34',9582341523,'nayakghana@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

# sql="insert into artist values (10,'Rajan','rajraj@12','Floral abstract','acrylic on canvas','12*12 inches',243000,'SQ34','9546281320','rajraj23@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

# sql="insert into artist values (11,'Paras','paras@23','Musical Ganesha','acrylic on canvas','36*12 inches',220000,'RT44','9986521420','paraspp23@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

# sql="insert into artist values (12,'suresh','susu@01','cityscope','acrylic on canvas','30*60 inches',124000,'ER90','9982531023','sureshsuresh12@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

# sql="insert into artist values (13,'Ganapathi hega','ganahana@12','saraswati','Oil on canvas','12*12 inches',100000,'US23','9963254172','ganapathi45@gmail.com')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")



pn = input("Enter your email :")
cb = input("Enter your password :")
mycursor.execute("use art_gallary")
mycursor.execute("select*from cust_cart")
myresult = mycursor.fetchall()
# print(myresult)
d = {1: 'id_no', 2: 'cust_gmail', 3: 'cust_password', 4: 'cust_name', 5: 'artist_password', 6: 'artist_gmail',
     7: 'painting_name', 8: 'mediam',
     9: 'size', 10: 'price', 11: 'paiment sts', 12: 'artist_name'}
# print(l)
dict = {}
t = 0
c = 0
for i in myresult:
    for x in i:
        # print(x)
        t = t + 1
        dict.setdefault(d.get(t), x)
    # print(dict)
    if pn == dict.get("painting_name") and cb == dict.get("artist_name"):
        mycursor.execute("use art_gallary")
        sql = "delete from cust_cart where cust_gmail=" + "'" + p + "'" + " and " + "cust_password=" + "'" + q + "'"
        mycursor.execute(sql)
        mydb.commit()
        print(" your records are carted")
        print("\n")

    dict = {}
    t = 0