li = []

for i in range(5) :
  li.append(int(input()))

li.sort()

average = 0

for i in range(5) :
  average += li[i]

average = int(average/5)

print(average)
print(li[2])