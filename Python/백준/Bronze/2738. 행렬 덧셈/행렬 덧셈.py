

N, M = map(int, input().split())

array1 = []
array2 = []


for i in range(N) :
  array1.append(list(map(int, input().split())))


for i in range(N) :
  array2.append(list(map(int, input().split())))



result = []

for i in range(N) :
  li = []
  for j in range(M) :
    li.append(array1[i][j] + array2[i][j])
  result.append(li)


for i in range(N) :
  print(*result[i])

