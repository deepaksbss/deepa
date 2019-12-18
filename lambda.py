""" lambda syntax square = (lambda a,b : a*b)
is anominace funtion """  

def square(num):
    return num * num

print(square(5))

# in this u can call the no function name use one time is easy

#lambda no function name


square = (lambda num : num)
num = [1,2,3,4]
print(square(num))


""" Map syntax :: double = list(map(lambda  num: num['deep'], num ))
is anominace funtion ** Map object which can be converted into
another data structure """  
num = [{'deep':'sai', 'bala':'sbss'},{'deep':'sai2', 'bala':'sbss'}]
double = list(map(lambda  num: num['deep'], num ))
print(double)

def decrement_list(l):
    return list(map(lambda n: n-1, l))



print(decrement_list([1,2,3]))

