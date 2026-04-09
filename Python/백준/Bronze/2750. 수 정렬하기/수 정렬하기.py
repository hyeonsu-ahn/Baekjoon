N = int(input())

li = []

for i in range(N) :
  li.append(int(input()))

result = sorted(li)

for i in range(len(result)) :
  print(result[i])


