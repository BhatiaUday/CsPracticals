# read text file and replace spaces from text FILE WITH A GIVEN CHARACTER

y=input("Enter char to replace spaces with: ")
f=open("file.txt","r")
x=f.read()
print(x.replace(" ", y))

f.close()