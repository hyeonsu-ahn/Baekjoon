ti = input().split()
C = int(input())
A = int(ti[0])
B = int(ti[1])

B += C

if B >= 60 :
  A += B // 60
  B = B % 60
  if A >= 24 :
    A = A%24

print(A , B)



