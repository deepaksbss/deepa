#Zip

num = [1,2,3,4]
num1 = [4,5,6,7]
z = (zip(num,num1))
print(z)


numb = [(0,1), (1,2), (2,3), (3,4), (4,5)]
print(list(zip(*numb)))

midterm = [80,91,78]
finals = [98,89,53]
students = ['dep', 'sbss', 'sai']

final_grades = [max(pair) for pair in zip(midterm, finals)]



print(final_grades)
final_grad = {t[0] : max(t[1], t[2]) for  t in zip(students, midterm,finals)}
print(final_grad)







lst =dict(zip(students, map(lambda pair : max(pair), zip(midterm, finals))))

print(lst)


#disct_val =dict(zip(students, map(lambda pair : ((pair[0]+pair[1]) /2), zip(midterm, finals))))

#print(disct_val)

    
    

