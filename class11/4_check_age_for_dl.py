#to check if user is eligible for drivers license
name=input("Enter your name: ")
age=int(input("Enter your age in years: "))
if age<18 :
    print(name+", You are not eligible for driver license")
else:
    print(name+", You are eligible for driver license")