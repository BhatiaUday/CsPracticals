#find all +ve and -ve numbers in a list of numbers

n = int(input("Enter how many numbers you want to enter: "))
List=[]
positive=[]
negative=[]
for i in range(n):
    number=int(input("Enter number in the list: "))
    List.append(number)
for i in range(n):
    if List[i]>=0 :
        positive.append(List[i])
    else:
        negative.append(List[i])
print("All +ve = ",positive)
print("All -ve = ",negative)
print("All Nums = ",List)