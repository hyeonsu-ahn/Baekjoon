n = list(map(int, list(input())))

result = 0

for i in range(len(n)) :
  result += n[i] ** 5
print(result)