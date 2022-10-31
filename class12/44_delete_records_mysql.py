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

def delinfo():
    iddel=int(input("Enter Emp ID to be deleted: "))
    cursor.execute("select * from empinfo where empid ="+str(iddel))
    for x in cursor:
        print (x)
    x=input("Do you want to delete this record?")
    if x=="Y":
        query="DELETE from empinfo where emp_id="+str(iddel)
        cursor.execute(query)
        cnx.commit()
        print("Deleted Info Successfully")
    elif x== "y":
        query="DELETE from empinfo where emp_id="+str(iddel)
        cursor.execute(query)
        cnx.commit()
        print("Deleted Info Successfully")
    elif x== "n":
        print("Operation cancelled")
    elif x== "N":
        print("Operation cancelled")
    else:
        print("Unknown option")
            