n = int(input("Enter how many numbers you want to enter: "))
List=[]
for i in range(n):
    number=int(input("Enter number in the list: "))
    List.append(number)
newList = []
for a in range(n):
    if List[a] not in newList:
        newList.append(List[a])
print("The list without any duplicate element is:",newList)