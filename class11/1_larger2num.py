#print larger of 2 user inputed numbers
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))

if(n1<n2):
    print(n1+ " is smaller than"+ n2 )
elif(n1>n2):
    print(n1+ " is greater than"+ n2)
else:
    print(n1+ " is equal to"+ n2)