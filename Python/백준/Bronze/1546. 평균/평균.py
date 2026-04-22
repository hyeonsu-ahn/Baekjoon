N = int(input())


test = list(map(int, input().split()))

maxpoint = max(test)

base = 100/maxpoint

for j in range(len(test)) :
  test[j] = test[j] * base

  
total = 0
for j in range(len(test)) :
  total += test[j]

print(total/len(test))
  