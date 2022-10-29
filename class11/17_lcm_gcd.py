#to find the lcm and gcd of 2 inputted numbers


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1>num2:
    higher=num1
    lcm= num1
    lower=num2
    hcf=num2
else:
    higher=num2
    lcm= num2
    lower=num1
    hcf=num1

while True:
    if lcm%lower==0 and lcm%higher==0 :
        break
    else:
        lcm = lcm + 1

print("LCM =", lcm)


while True:
    if lower%hcf==0 and higher%hcf==0:
        break
    else:
        hcf=hcf-1