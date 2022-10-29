#find largest number in list of numbers

n = int(input("Enter how many numbers you want to enter: "))
List=[]
largest=0
for i in range(n):
    number=int(input("Enter number in the list: "))
    List.append(number) 
print(list)
for i in range(n):
    if largest<List[i]:
        largest=List[i]
print("The largest number in the list is ",  largest)