import mysql.connector as mysql

uname=input("Username(root is default)") or "root"
pwd=input("Pwd(No default value)")
serverip=input("Server address(enter for default)") or "localhost"
cnx = mysql.connect(user=uname, password=pwd,host=serverip)
cursor= cnx.cursor()
try:
    cursor.execute("create database database1")
except:
    pass
cursor.execute("use database1")

def newemp():
    eid=int(input("Enter Employee ID: "))
    ename=input("Enter Employee Name: ")
    e_no=int(input("Enter Employee Phone Number: "))
    eaddr=input("Enter Employee Address: ")
    data=str(eid)+","+"'"+str(ename)+"'"+","+str(e_no)+","+"'"+str(eaddr)+"'"
    query="insert into empinfo values ("+data+")"
    cursor.execute(query)
    cnx.commit()
    cursor.execute("select * from empinfo where empid ="+str(eid))
    for x in cursor:
        print (x)

newemp()