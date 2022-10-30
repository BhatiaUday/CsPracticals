# Remove all the lines that contain the character 'a' in a file and write it to another file

f=open("file.txt","r")
f1=open("file1.txt","w")

lines=f.readlines()
loop=0
for i in lines:
    loop=1
    for x in i:
        if x=="a" and loop==1 :
            f1.write(i)
            f1.write("\n")
            loop=0

f.close()
f1.close()