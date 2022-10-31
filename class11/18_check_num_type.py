#to check if the number is an Armstrong number or not

num = int(input("Enter a number: "))
x = 0
temp = num
while temp > 0:
   digit = temp % 10
   x += digit ** 3
   temp = temp // 10

if num == x:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")