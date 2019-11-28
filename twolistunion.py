n  = int(input("Enter the values in the first"))
list1 =[]
for i in range(n):
    b = int(input("enter the values"))
    list1.append(b)
secondlist = int(input("Enter the values in the second"))
list2 = []
for i in range(secondlist):
    c = int(input("Enter the values"))
    list2.append(c)
    
answer = [i for i in list1 for i  in list2]
print(answer)
