#display largest of n numbers inputted
n=int(input("Enter the amout of numbers you want to compare: "))
x=[]
for i in range(n):
    y=int(input("Enter number"))
    x.append(y)
print("the largest number is " + str(x.max()))