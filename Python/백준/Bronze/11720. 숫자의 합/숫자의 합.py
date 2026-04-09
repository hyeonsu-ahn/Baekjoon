N = int(input())


li = list(map(int, list(input())))
result = 0
for i in range(N) :
  result += li[i]

print(result)
