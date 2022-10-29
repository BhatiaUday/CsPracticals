#to give sum of numbers entered by the user
sum=0
print
while True:
    try:
        print("The current sum is "+ str(sum) )
        x=int(input("Enter number you want to add: "))
        sum=sum+x
        print("Type Clear to clear the sum")
    except:
        sum=0