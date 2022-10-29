n=int(input("enter length of sequence: "))
x=1
y=x*x*x
inv=1/y
for i in range(n):
    sum+=inv
    x=x+1
    y=x*x*x
    inv=1/y