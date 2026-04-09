A, B = map(list, input().split())

reA = ''
reB = ''

for i in range(len(A)-1,-1, -1):
  reA += A[i]

for i in range(len(B)-1,-1, -1):
  reB += B[i]

if int(reA) > int(reB) :
  print(int(reA))
else :
  print(int(reB))