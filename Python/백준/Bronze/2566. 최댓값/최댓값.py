sqaure = []

for i in range(9) :
  sqaure.append(list(map(int, input().split())))

bestnum = sqaure[0][0]
bestindex = [0, 0]
for i in range(9) :
  for j in range(9) :
    if bestnum < sqaure[i][j] :
      bestnum = sqaure[i][j]
      bestindex = [i, j]

print(bestnum)
print(bestindex[0]+1, bestindex[1]+1)
