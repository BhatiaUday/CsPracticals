n = int(input("Enter number of students : "))
list1=[]
for i in range(n):
    email=input("Enter email: ")
    list1.append(email)
tuple1=tuple(list1)
names=[]
domains=[]
for i in tuple1:
    name,domain = i.split("@")
    names.append(name)
    domains.append(domain)
names = tuple(names)
domains = tuple(domains)
print("Names = ",names)
print("Domains = ",domains)
print("Tuple = ",tuple1)
