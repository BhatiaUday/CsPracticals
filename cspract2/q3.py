n=int(input("enter the number of emails you want to enter"))
c=1
temp1=input("enter your email id")
username=(temp1.split("@")[0])
domain=(temp1.split("@")[1])
while c<n:
    temp=input("enter your email id")
    username=username+" , "+temp.split("@")[0]
    domain=domain+" , "+temp.split("@")[1]
    temp1=temp1+" , "+temp
    c=c+1
t1={temp1}
print(t1)
user={username}
dom={domain}
print(user)
print(dom)