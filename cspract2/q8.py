n = int(input("Enter how many numbers you want to enter: "))
List=[]
for i in range(n):
    number=int(input("Enter number in the list: "))
    List.append(number)
print(List, "is your given list.")
List.sort()
print(List, "is the sorted list.")
c = len(List)
if c%2 != 0:
    med = c//2
    print(List[med], "is the median.")
else:
    a = List[c//2]
    b = List[(c//2) - 1]
    s = a + b
    med = s/2
    print(med, "is the median.")