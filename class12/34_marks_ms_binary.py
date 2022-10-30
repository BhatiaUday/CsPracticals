#Create a binary file with roll number name and marks input a roll number and update the marks and delete the record

import pickle


def add_data():
    f=open("data.dat","rb")
    data1=[]
    try:
        x=pickle.load(f)
        for i in x:
            data1.append(i)
    except:
        pass
    f.close()
    n=int(input("Enter number of records you want to enter: "))
    for i in range(n):
        rno=int(input("Enter roll number: "))
        name=input("Enter name: ")
        marks=float(input("Enter marks: "))
        data=[rno,name,marks]
        data1.append(data)
    f.close()
    f=open("data.dat","wb")
    pickle.dump(data1,f)
    f.close()

def update_data():
    f=open("data.dat","rb")
    x=pickle.load(f)
    f.close()
    n=int(input("Enter roll no of who you wan to update the marks of: "))
    data1=[]
    for i in x:
        if i[0]==n:
            name=input("Enter name: ")
            marks=float(input("Enter marks: "))
            data=[n,name,marks]
            data1.append(data)
        else:
            data1.append(i)
    f=open("data.dat","wb")
    pickle.dump(data1,f)
    f.close()


def delete_data():
    f=open("data.dat","rb")
    x=pickle.load(f)
    f.close()
    n=int(input("Enter roll no of who you wan to delete: "))
    data1=[]
    for i in x:
        if i[0]==n:
            pass
        else:
            data1.append(i)
    f=open("data.dat","wb")
    pickle.dump(data1,f)
    f.close()

def menu():
    print("1.Enter records\n2.Update records\n3.Delete records\n4Print records")

while True:
    menu()
    i=int(input("Enter your choice: "))
    if i==1:
        add_data()
    if i==2:
        update_data()
    if i==3:
        delete_data()
    if i==4:
        f=open("data.dat","rb")
        x=pickle.load(f)
        f.close()
        for i in x:
            print(i)