N, M = map(int, input().split())

castle = []

for i in range(N) :
  castle.append(list(input()))
  
needrow = 0
needcol = 0

for i in range(N) :
  if castle[i].count("X") == 0 :
    needrow += 1

for i in range(M) :
  for j in range(N) :
    if castle[j][i] == 'X' : 
      break
    if j == N-1 :
      needcol +=1

if needrow < needcol :
  print(needcol) 
else :
  print(needrow)