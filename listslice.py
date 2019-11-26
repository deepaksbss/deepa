a = []
n = int(input("Enter the number of values"))
for i in range(1, n+1):
    b = int(input("Enter the values"))
    a.append(b)

a.sort()
print(a)
print("this is the largest number{}". format(a[n-2]))

