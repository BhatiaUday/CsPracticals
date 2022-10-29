# to check for palendrome
from re import L


x=int(input("Enter the number you want to check for palendrome: "))
y=str(x)
z=y[::-1]
if z==y:
    print( y+"is a palendrome")
else:
    print( y+ "is not a palendrome")