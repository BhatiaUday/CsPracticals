n = int(input("Enter the number of students: "))
list1 = []
for i in range(n):
    name = input("Enter name of student: " ) 
    list1.append(name)
tuple1 = tuple(list1)
findingname = input("Enter name to find: ")
for item in tuple1:
    if item==findingname:
        print("Name found")
    else:
        found=1

if found==1:
    print ("name not found")
