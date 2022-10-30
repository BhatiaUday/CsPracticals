#Write a program to find the total occurrences of a specific words from a text file:

word=input("Enter word you want to count: ")
f=open("file.txt", "r")
y=f.read()
x=y.split()
count=0
for i in x:
    if i==word:
        count+=1
print(count)