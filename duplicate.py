a = []
n = int(input("Enter the number of the elements in the list"))
for i in range(0,n):
    element = int(input("Enter the elements" + str(i+1)))
    a.append(element)
b = set()
unique =[]

for i in a:
    if i not in b:
        unique.append(i)
        b.add(i)
print("non-duplicate items:")
print(unique)
