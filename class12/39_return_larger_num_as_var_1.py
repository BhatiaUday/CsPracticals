#Write a program that has a user defined function to accept 2 numbers as parameters, if number 1 is less
#than number 2 then numbers are swapped and returned

def largenum():
    global num1
    global num2
    if num1>num2:
        return
    if num2>num1:
        num1,num2=num2,num1
while True:
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))

    largenum()

    print("Num 1 variable is", num1)
    print("Num 2 variable is ", num2)