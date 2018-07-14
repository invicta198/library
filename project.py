#PROGRAM STARTS

import sqlite3,os,re,mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password"
)
mycursor = mydb.cursor()
try:
	mycursor.execute("CREATE DATABASE if not exists library")
except:
	print "ERROR IN CONNECTION"
conn=sqlite3.connect("library")
mycursor1=conn.cursor();
mycursor2=conn.cursor();
mycursor3=conn.cursor();
mycursor4=conn.cursor();
mycursor5=conn.cursor();
try:
    mycursor1.execute("Create table if not exists login(lid varchar(5) primary key,password varchar(20),name varchar(20),role varchar(10))")
    mycursor2.execute("Create table if not exists book(bid varchar(5) primary key,title varchar(20),subject varchar(20),author varchar(20),status varchar(20))")
    mycursor3.execute("Create table if not exists student(roll varchar(5) primary key,name varchar(20),dept varchar(5),sem varchar(5),batch varchar(5),password varchar(20))")
    mycursor4.execute("Create table if not exists employee(id varchar(5) primary key,name varchar(20),dept varchar(5),joindate varchar(20),password varchar(20))")
    mycursor5.execute("Create table if not exists issue(id varchar(5) primary key,status varchar(20))")
    conn.commit()
except Exception as e:
    print (e),"\ln##### SOMETHING WRONG IN CREATING EITHER OF THE TABLE #####"

#CONNECTION SET,DATABASE OPENED,CONTROL OF PROGRAM STARTS"

sql="insert into login values(?,?,?,?)"
value=["16409","1234","avijit","employee"]	#"ADMIN"
mycursor1.execute(sql,value)
sql="insert into login values(?,?,?,?)"
value=["7374","1234","anijit","student"]	#"FIRST STUDENT"
mycursor1.execute(sql,value)
print"------------------------------------------------------------\n",
print"      WELCOME TO COLLEGE LIBRARY PANEL"									#"WELCOME PANEL"
print"------------------------------------------------------------\n",
ch = "a"
while ch != "c":
    print"\nSELECT THE GIVEN OPTIONS:"
    print"a:for login\nb:for registration\nc:for exit"
    print"---------------------------------------------------\n",
    ch=raw_input("ENTER YOUR CHOICE: ")
    if ch=="a":
        c=[]
        loginid=raw_input("ENTER LOGIN ID: ")
        mycursor1.execute("Select lid from login")
        for i  in mycursor1:
            c.append(i[0])
        for i in c:
            if i == loginid:
                k = 1
                break
            else:
                k = 0
        if k>0:
            password = raw_input("ENTER PASSWORD: ")
            c=[]
            mycursor1.execute("Select password from login")
            for i in mycursor1:
                c.append(i[0])
            for i in c:
                if i==password:
                    l=1
                    break
                else:
                    l=0
            if l>0:
                sql="Select role from login where lid=?"
                value=[loginid]
                mycursor1.execute(sql,value)
                for i in mycursor1:
                    for j in i:
                        s=j
                if s=="employee":
                    login_emp()
                elif s=="student":
                    login_std()
				#else:
				#	print"##### INVALID CHOICE #####"
            else:
                print"##### PASSWORD IS WRONG #####"
        else:
            print"##### MAY BE YOU ARE NOT REGISTERED #####"
    elif ch=="b":
        print"---------------------------------------------------\n",
        print"a:REGISTER STUDENT\nb:REGISTER EMPLOYEE"
        print"---------------------------------------------------\n",
        ch2=raw_input("ENTER CHOICE: ")
        if ch2=="a":
            sign_std()
        elif ch2=="b":
            sign_emp()
        else:
            print"##### INVALID CHOICE #####"
    elif ch=="c":
        print"******* THANK YOU! VISIT AGAIN *******"
        break;
    else:
        print"##### INVALID CHOICE #####"

def sign_emp():																# REGISTRATION OF EMPLOYEE FUNCTION
    flag=0;
    print"REGISTER EMPLOYEE HERE:\n"
    id = raw_input("ENTER 4 DIGIT ID")
    if re.match('[0-9]{4}',id) and len(id)==4:
        flag=1
    while flag==0:
        id=raw_input("ENTER 4 DIGIT ID")
        if re.match('[0-9]{4}', id) and len(id) == 4:
            flag = 1
    flag=0
    name=raw_input("ENTER NAME")
    if re.match('[a-zA-Z]\s',name):
        flag=1
    while flag==0:
        name=raw_input("ENTER NAME")
        if re.match('[a-zA-Z]\s', name):
            flag = 1
    flag=0
    dept=raw_input("ENTER DEPARTMENT")
    if re.match('[a-zA-Z]',dept):
        flag=1
    while flag==0:
        dept=raw_input("ENTER DEPARTMENT")
        if re.match('[a-zA-Z]', dept):
            flag = 1
    flag=0
    join=raw_input("ENTER JOIN DATE")
    password=raw_input("ENTER PASSWORD")
    sql="insert into employee values(?,?,?,?,?)"
    value=[id,name,dept,join,password]
    mycursor4.execute(sql,value)
    sql="insert into login(?,?,?,?)"
    value = [id,password,name,dept]
    mycursor1.execute(sql, value)
    print "******* REGISTRATION SUCCESSFULL *******"

def login_emp():																# LOGIN FUNCTION FOR EMPLOYEE	
    print"---------------------------------------------------\n",
    print"a:ADD BOOK\nb:FOR DELETE BOOK\nc:FOR LIST ALL BOOKS\nd:FOR SEARCH BOOK\ne:FOR ISSUE BOOK\nf:FOR ADD NEW EMPLOYEE\ng:FOR EXIT"
    print"\n-------------------------------------------------\n"
    ch=raw_input("ENTER CHOICE: ")
    if ch=="a":
        addbook_emp()
    elif ch=="b":
        delbook_emp()
    elif ch=="c":
        viewbook()
    elif ch=="d":
        searchbook()
    elif ch=="e":
        issuebook_emp()
    elif ch=="f":
        sign_emp()
    elif ch=="g":
        print"******* BACK TO HOME SCREEN *******"
    else:
        print"####### INVALID CHOICE ######"

def addbook_emp():															# ADDING BOOK TO LIBRARY FUNCTION
    flag=0
    id = raw_input("ENTER 4 DIGIT BOOK ID")
    if re.match('[0-9]{4}', id) and len(id) == 4:
        flag = 1
    while flag == 0:
        id = raw_input("ENTER 4 DIGIT BOOK ID")
        if re.match('[0-9]{4}', id) and len(id) == 4:
            flag = 1
    flag = 0
    title = raw_input("ENTER TITLE")
    if re.match('[a-zA-Z]\s',title):
        flag=1
    while flag==0:
        title=raw_input("ENTER TITLE")
        if re.match('[a-zA-Z]\s', title):
            flag = 1
    flag=0
    sub = raw_input("ENTER SUBJECT")
    if re.match('[a-zA-Z]\s',sub):
        flag=1
    while flag==0:
        sub=raw_input("ENTER SUBJECT")
        if re.match('[a-zA-Z]\s', sub):
            flag = 1
    flag=0
    author = raw_input("ENTER AUTHOR")
    if re.match('[a-zA-Z]\s',author):
        flag=1
    while flag==0:
        author=raw_input("ENTER AUTHOR")
        if re.match('[a-zA-Z]\s', author):
            flag = 1
    sql = "insert into book values(?,?,?,?,?)"
    value = [id,title,sub,author,"Available"]
    mycursor2.execute(sql, value)
    print "******* ADDITION SUCCESSFULL *******"

def delbook_emp():													# DELETION OF BOOK FROM LIBRARY SYSTEM
    flag = 0
    id = raw_input("ENTER 4 DIGIT BOOK ID")
    if re.match('[0-9]{4}', id) and len(id) == 4:
        flag = 1
    while flag == 0:
        id = raw_input("ENTER 4 DIGIT BOOK ID")
        if re.match('[0-9]{4}', id) and len(id) == 4:
            flag = 1
    sql = "delete from book where id=?"
    value = [id]
    mycursor2.execute(sql, value)
    print "******* DELETION SUCCESSFULL *******"

def viewbook():														# VIEW DETAILS OF REQUIRED BOOK
    mycursor2.execute("Select * from book")
    for i in mycursor2:
        print i[0],i[1],i[2],i[3],i[4]

def searchbook():													# SEARCH A BOOK IN LIBRARY OF REQUIRED GENER
    flag=0
    print"SEARCH BOOK HERE:\n"
    sub = raw_input("ENTER SUBJECT:")
    if re.match('[a-zA-Z]\s', sub):
        flag = 1
    while flag == 0:
        sub = raw_input("ENTER SUBJECT")
        if re.match('[a-zA-Z]\s', sub):
            flag = 1
    sql="Select * from book where subject=?"
    value=[sub]
    mycursor2.execute(sql,value)
    for i in mycursor2:
        print i[0],i[1],i[2],i[3],i[4]

def issuebook_emp():												# ISSUE A BOOK TO STUDENT BY EMPLOYEE
    flag = 0
    id = raw_input("ENTER 4 DIGIT BOOK ID")
    if re.match('[0-9]{4}', id) and len(id) == 4:
        flag = 1
    while flag == 0:
        id = raw_input("ENTER 4 DIGIT BOOK ID")
        if re.match('[0-9]{4}', id) and len(id) == 4:
            flag = 1
    flag=0
    roll = raw_input("ENTER 6 DIGIT ROLL NUMBER")
    if re.match('[0-9]{6}', roll) and len(roll) == 6:
        flag = 1
    while flag == 0:
        roll = raw_input("ENTER 6 DIGIT ROLL NUMBER")
        if re.match('[0-9]{6}', roll) and len(roll) == 6:
            flag = 1
    c=[]
    mycursor2.execute("Select bid from book")
    for i in mycursor2:
        c.append(i[0])
    for i in c:
        if i == id:
            k = 1
            break
        else:
            k = 0
    if k>0:
        c = []
        mycursor1.execute("Select lid from login")
        for i in mycursor1:
            c.append(i[0])
        for i in c:
            if i == roll:
                k = 1
                break
            else:
                k = 0
        if k>0:
            c = []
            sql="Select status from book where bid=?"
            value=[id]
            mycursor2.execute(sql, value)
            for i in mycursor1:
                for j in i:
                    x=j
            if x=="Available":
                value = ["ISSUED",id]
                sql = "update book set status=? where bid=?"
                mycursor2.execute(sql, value)
                print"******* BOOK ISSUED TO "+roll+" *******"
            else:
                print"####### BOOK NOT AVAILABLE #######"
        else:
            print"####### BOOK ISSUE ERROR #######"
    else:
        print"####### BOOK ISSUE ERROR #######"

def sign_std():																# REGISTRATION OF A STUDENT IN LIBRARY PANEL
    flag=0
    print"REGISTER STUDENT HERE:\n"
    id = raw_input("ENTER 6 DIGIT ROLL NUMBER")
    if re.match('[0-9]{6}', id) and len(id) == 6:
        flag = 1
    while flag == 0:
        id = raw_input("ENTER 6 DIGIT ROLL NUMBER")
        if re.match('[0-9]{6}', id) and len(id) == 6:
            flag = 1
    flag = 0
    name = raw_input("ENTER NAME")
    if re.match('[a-zA-Z]\s', name):
        flag = 1
    while flag == 0:
        name = raw_input("ENTER NAME")
        if re.match('[a-zA-Z]\s', name):
            flag = 1
    flag = 0
    dept = raw_input("ENTER DEPARTMENT")
    if re.match('[a-zA-Z]', dept):
        flag = 1
    while flag == 0:
        dept = raw_input("ENTER DEPARTMENT")
        if re.match('[a-zA-Z]', dept):
            flag = 1
    flag = 0
    sem = raw_input("ENTER SEMESTER")
    if re.match('[0-9]{1}', sem) and len(sem) == 1:
        flag = 1
    while flag == 0:
        sem = raw_input("ENTER SEMESTER")
        if re.match('[0-9]{1}', sem) and len(sem) == 1:
            flag = 1
    flag = 0
    batch = raw_input("ENTER BATCH")
    if re.match('[0-9]{4}', batch) and len(batch) == 4:
        flag = 1
    while flag == 0:
        batch = raw_input("ENTER BATCH")
        if re.match('[0-9]{4}', batch) and len(batch) == 4:
            flag = 1
    password = raw_input("ENTER PASSWORD")

    sql = "insert into student values(?,?,?,?,?,?)"
    value = [id, name, dept, sem, batch, password]
    mycursor3.execute(sql, value)
    sql = "insert into login(?,?,?,?)"
    value = [id, password, name, dept]
    mycursor1.execute(sql, value)
    print "******* REGISTRATION SUCCESSFULL *******"

def login_std():															# LOGIN OF A REGISTERED STUDENT
    print"a:FOR VIEW ALL BOOKS\nb:FOR SEARCH BOOK\nc:FOR EXIT"
    print"\n-------------------------------------------------\n"
    ch =input("ENTER YOUR CHOICE")
    if ch == "a":
        viewbook()
    elif ch == "b":
        searchbook()
    elif ch == "c":
        return
    else:
        print"####### INVALID CHOICE #######"
		
#	-----------------------------------------------------------------ENDS-----------------------------------------------------------------------#
#	-----------------------------------------------------------------ENDS-----------------------------------------------------------------------#