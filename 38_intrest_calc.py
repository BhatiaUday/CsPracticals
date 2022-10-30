#Write a program that implements a user defined function that accepts Principal Amount, Rate, Time,
#Number of Times the interest is compounded to calculate and displays compound interest. (Hint: CI =((P*(1+R/N))NT

def compound(principle,rate,time):
    intrest=principle*pow((1+rate),time)
    print("The total payment is", intrest)

while True:

    p=int(input("Enter the principle: "))
    r=int(input("Enter interest rate (in %): "))
    t=int(input("Enter time period (in years)"))
    compound(p,r,t)
