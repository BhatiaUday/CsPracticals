#Write a program that contains user defined functions to calculate area, perimeter or surface area
#whichever is applicable for various shapes like rectangle, cuboid, triangle, sphere and cylinder. The user
#defined functions should accept the values for calculation as parameters and the calculated value should be
#returned. Import the module and use the appropriate functions.
import math
def rectangle(x,y):
    perm = 2*(x+y)
    print("Perimeter of rectangle is",perm)
    area = x*y
    print("Area of rectangle is",area)
def cuboid(x,y,z):
    surface=2*(x*y+y*z+z*x)
    print("Surface area of cuboid is",surface)
    volume=x*y*z
    print("Volume of cuboid is",volume)
def triangle(a,b,c):
    perm=a+b+c
    print("The perimeter of the triangle is", perm)
    s=(a+b+c)/2
    a2=s*(s-a)*(s-b)*(s-c)
    a=math.sqrt(a2)
    print("The area of the triangle is ",a)
def sphere(r):
    surfacear=4*3.14*r*r
    print("The surface area of the sphere is",surfacear)
    vol=4*3.14*r*r*r/3
    print("The vol of the sphere is ", vol)
def cylender(h,r):
    surfarea=(2*3.14*r*r)+(2*3.14*r*h)
    print("The surface area of the cylender is ", surfarea)
    volume=3.14*r*r*h
    print("The volume of the cylender is ", volume)

while True:
    print("1. Rectangle")
    print("2. Cuboid")
    print("3. Triangle")
    print("4. Sphere")
    print("5. Cylinder")
    print("6. Exit")
    x=int(input("Enter your choice:"))
    if x==1:
        x=int(input("Enter length:"))
        y=int(input("Enter breadth: "))
        rectangle(x,y)
    if x==2:
        x=int(input("Enter length:"))
        y=int(input("Enter breadth: "))
        z=int(input("Enter height: "))
        cuboid(x,y,z)
    if x==3:
        a=int(input("Enter side 1:"))
        b=int(input("Enter side 2: "))
        c=int(input("Enter side 3: "))
        triangle(a,b,c)
    if x==4:
        r=int(input("Enter radius of sphere: "))
        sphere(r)
    if x==5:
        r=int(input("Enter radius of cylinder: "))
        h=int(input("Enter height of cylinder: "))
        cylender(h,r)
    if x==6:
        break