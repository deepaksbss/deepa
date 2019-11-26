first =[]
n1 = int(input("Enter the number:"))
for i in range(1, n1+1):
    b = int(input("Enter the values"))
    first.append(b)
second =[]
n2 = int(input("Enter the number:"))
for i in range(1, n2+1):
    c = int(input("enter the values"))
    second.append(c)
mainarray = first + second;
print(mainarray)
mainarray.sort()
print("this is the sort element", mainarray)
