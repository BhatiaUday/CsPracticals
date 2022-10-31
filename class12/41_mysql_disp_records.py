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

cursor.execute("select * from table")
for x in cursor:
        print(x)