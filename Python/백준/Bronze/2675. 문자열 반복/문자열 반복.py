T = int(input())

for i in range(T) :
  r, S = map(list, input().split())
  R = int(r[0])
  result = []
  for j in range(len(S)) :
    result.append(S[j]*R)

  print("".join(result))

