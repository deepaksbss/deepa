answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
print(answer)
answer1 =[val[::-1].lower() for val in ["Deepak", "neeha", "maati"]]
print(answer1)
answer2 = [i for i in range(1,101) if (i % 13) == 0]
print(answer2)
answer3 = [i for i in "amazing" if i not in "aeiou"]
print(answer3)

var = [[1,2,3],[4,5,6],[7,8,9]]
for i in var:
    for var1 in i :
        print(var1)

answer4 = [[i for i in range(0,3)] for i in range(0, 3)]
print(answer4)
answer5 = [[i for i in range(0, 10)] for i in range(0,10)]
print(answer5)
