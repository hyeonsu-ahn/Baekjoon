li = []
for i in range(10) :
  x = int(input())%42
  if li.count(x) == 0 :
    li.append(x)

print(len(li))
