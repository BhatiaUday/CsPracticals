# sum all the numbers in user string

x=input("Enter String")
sum=0
for i in x:
    if i.isdigit()== True:
        sum=sum+int(i)