#find the 2 largest numbers in the list of numbers

n = int(input("Enter how many numbers you want to enter: "))
List=[]
largest=0
large2=0
for i in range(n):
    number=int(input("Enter number in the list: "))
    List.append(number) 
for i in range(n):
    if largest<List[i]:
        large2=largest
        largest=List[i]
print("The largest number in the list is ",  largest)
print("The 2nd largest number in the list is ",  large2)