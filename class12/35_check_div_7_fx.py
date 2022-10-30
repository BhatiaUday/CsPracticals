#Write a program to check the divisibility of a number by 7 that is passed as a parameter to the user defined function

def divbyseven(number):
    if number % 7 == 0:
        return True
    else:
        return False
while True:
    x=int(input("Enter number to check divisibility by 7: "))

    print(divbyseven(x))