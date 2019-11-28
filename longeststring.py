a = []
n = int(input("Enter the number of elements list"))
for i in range(n):
    elements= input("Enter the elements")
    a.append(elements)
max1 = len(a[0])
temp = a[0]
for i in a:
    if(len(i)>max1):
        max1=len(i)
        temp = i
print(temp)
