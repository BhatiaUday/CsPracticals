n = int(input("Enter the number of students: "))
t=0
List = []
for i in range(n):
    name = input("Enter Name: ") 
    List.append(name)
tuple1 = tuple(List)
findName = input("Enter name to find: ")
for item in tuple1:
    if item==findName:
        print("Name found")
        t=1
if t==0:
    print("Name not found")