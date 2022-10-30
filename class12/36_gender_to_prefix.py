#Write a program that uses a user defined function that accepts name and gender (as M for Male, F for Female) and prefixes Mr/Ms on the basis of the gender.

def nametoprefix(name,gender):
    if gender == "M":
        print("Mr." + name )
    elif gender == "F":
        print("Ms." + name )
    else:
        print("Invalid gender input")
while True :
    name = input("Enter your name: ")
    gender = input("Enter your gender (M for Male, F for Female): ")
    gender=gender.upper()
    nametoprefix(name,gender)