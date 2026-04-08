n = list(input())
result = 1
for i in range(int(len(n)/2)) :
  if n[i] != n[(len(n)-1) - i] :
    result = 0

print(result)
