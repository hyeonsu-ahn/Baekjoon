end = False

while not end:

  A, B, C = map(int, input().split())

  if A == 0 and B == 0 and C == 0 :
    end = True
    break
  is_right = 0 #0은 직각 아님

  maxnum = A
  if maxnum < B :
    maxnum = B
  if maxnum<C :
    maxnum = C

  if maxnum == A :
    if A**2 == B**2 + C**2 :
      is_right = 1
  if maxnum == B :
    if B**2 == A**2 + C**2 :
      is_right = 1
  if maxnum == C :
    if C**2 == A**2 + B**2 :
      is_right = 1

  if is_right == 1 :
    print("right")
  else :
    print("wrong")

