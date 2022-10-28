#to find if the number is prime or composite
x= int(input("Enter the number you want to check: "))
for i in range(x):
    if x%i==0:
        print(x+" is composite")
        break
else:
    print(x+" is prime")
