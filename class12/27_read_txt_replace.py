# read text file and replace " " with "#"

f=open("file.txt","r")
x=f.read()
print(x.replace(" ", "#"))

f.close()