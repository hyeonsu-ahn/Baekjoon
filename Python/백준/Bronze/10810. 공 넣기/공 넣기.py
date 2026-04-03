N, M = map(int, input().split())
li = []
for p in range(N) :
    li.append(0)
for p in range(M) :
    i, j , k = map(int, input().split())
    for h in range(i-1, j) :
        li[h] = k
    

for p in range(N) :
    print(li[p], end=' ')