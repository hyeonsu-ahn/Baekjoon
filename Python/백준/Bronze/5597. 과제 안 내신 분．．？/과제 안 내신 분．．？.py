di = {}
for i in range(1, 31) :
    di.update({i:0})

for i in range(28) :
    di[int(input())] = 1

li = list(di.items())
for i in range(30) :
    if li[i][1] == 0 :
        print(li[i][0])
