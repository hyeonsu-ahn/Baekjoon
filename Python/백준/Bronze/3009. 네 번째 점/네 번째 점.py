a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

x = a[0]
y = a[1]

result = []
if x != b[0] :
  if x != c[0] :
    result.append(x)
  else :
    result.append(b[0])
else :
  result.append(c[0])

if y != b[1] :
  if y != c[1] :
    result.append(y)
  else :
    result.append(b[1])
else :
  result.append(c[1])



print(result[0], result[1])

