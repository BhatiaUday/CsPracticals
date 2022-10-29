#make list and add element to specific index


n = int(input("Enter the number of elements: "))
text=""
loop=1
List=[]
for i in range(n):
    number=int(input("Enter number in the list: "))
    List.append(number)
print(List, "is the orignal list.")
while loop==1:
    index = int(input("Enter the index position: "))-1
    num = eval(input("Enter the new element: "))
    List.insert(index, num)
    print(List, "is the new list.")
    text=input("Do you want to enter another element(y/n): ")
    if text=="n":
        loop=0