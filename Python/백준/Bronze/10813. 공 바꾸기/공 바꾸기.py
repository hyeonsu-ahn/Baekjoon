N, M = map(int, input().split())
li = []
for p in range(N) :
    li.append(p+1)

for p in range(M) :
    i, j = map(int, input().split())
    temp = li[i-1]   
    li[i-1] = li[j-1]
    li[j-1] = temp
    

for p in range(N) :
    print(li[p], end=' ')