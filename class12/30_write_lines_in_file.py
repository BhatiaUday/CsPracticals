#Write a program to create a text file “MyFile.txt” in python and ask the user to write separate 3 lines with three input statements from the user

f=open("myfile.txt","w")
for i in range(3):
    x=input("Enter a line: ")
    f.write(x+"\n")

f.close()