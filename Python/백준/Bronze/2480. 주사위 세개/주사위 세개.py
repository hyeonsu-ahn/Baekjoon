di = input().split()
A = int(di[0])
B = int(di[1])
C = int(di[2])

if A == B and B == C:
    print(10000 + (A*1000))
elif (A == B and A != C) or (A == C and A != B):
  print(1000 + (A*100))
elif B == C and B != A :
  print(1000 + (B*100))
else :
  di.sort()
  print(int(di[2]) * 100)




