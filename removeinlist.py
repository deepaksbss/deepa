a = []
n = int(input("Enter the number of elements in list"))
for x in range(n):
    element=input("Enter the elemnts")
    a.append(element)
print(a)
c = []
count=0
b = input("Enter the words to remove:")
n = int(input("enter the number of occurrence to remove"))
for i in a:
    if(i == b):
        count=count+1
        if(count!=n):
            c.append(i)
    else:
        c.append(i)
if(count==0):
    print("Iten not found")
else:
    print("the number of repetitions is:", count)
    print("udated list is:",c)
    print("The distinct elements are: ",set(a))
