total = int(input())
n = int(input())

for i in range(n) :
  items = input().split()
  it = int(items[0])
  um = int(items[1])

  total -= it*um

if total == 0 :
  print("Yes")
else :
  print("No")

