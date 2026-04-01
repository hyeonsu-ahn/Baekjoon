ti = input().split()
H = int(ti[0])
M = int(ti[1])

if M < 45 :
  M += 60
  H -= 1
  M -= 45
  if H < 0:
    H += 24
  print(H, M)
else :
  print(H, M-45)



