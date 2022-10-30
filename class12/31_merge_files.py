#Write a program to read the contents of two files and merge the contents into “merge.txt” avoid using the close() function

with open("file1.txt","r") as f1:
    x=f1.read()
with open("file2.txt","r") as f2:
    y=f2.read()
with open("merge.txt","w") as f:
    f.write(x+y)