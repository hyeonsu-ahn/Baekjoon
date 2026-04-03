N, M = map(int, input().split())
li = []
for i in range(N) :
    li.append(i+1)

for i in range(M) :
    i, j = map(int, input().split())
    temp = []
    for h in range(j, i-1, -1) :
        temp.append(li[h-1])
    index = i-1
    for h in range(len(temp)) :
        li[index] = temp[h]
        index += 1

for i in range(N) :
    print(li[i], end=" ")