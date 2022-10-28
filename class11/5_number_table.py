#print the table of a number inputted by the user
x=int(input("Enter Number: "))
print("Table of "+str(x)+"is:")
for i in range(10):
    y=i+1
    z=x*y
    print(z)