users = [{"userName": 'aaideepak',"keys":"deepusbss"},
         {"userName":'mbss'},
         {"userName":"deepu"}]

lst = [6,2,43,24]
print(sorted(lst, reverse= True))


sort = sorted(users, key=lambda users: users['userName'], reverse = True)
print(sort)




#Max and min
print(max(lst))
print(min(lst))

maxval = min(users, key=lambda users: users['userName'])['keys']
print(maxval)


#reversed


reversed("hello")
print(list(reversed("hello")))


for i in reversed(range(0,29)):
    print(i)






