N = int(input())
want = int(input())


# (i,j)좌표인 달팽이 배열
def recursive_snail(snail, n, want) :
  if n == 1 :
    if want == 1:
        snail['want'] = (0,0)
    snail[(0,0)] = 1
    return snail
  else :
    snailNum = n**2
    #왼쪽끝채움
    for j in range(int((n-1)/2),-int((n-1)/2)-1, -1) :
      if want == snailNum :
        snail['want'] = (-int((n-1)/2),j)
      snail[(-int((n-1)/2),j)] = snailNum
      snailNum -= 1
  
    #아래면 채움
    for i in range(-int((n-1)/2)+1,int((n-1)/2)+1) :
      if want == snailNum :
        snail['want'] = (i,-int((n-1)/2))
      snail[(i,-int((n-1)/2))] = snailNum
      snailNum -= 1
    
    #우측면 채움
    for j in range(-int((n-1)/2)+1, int((n-1)/2) +1) :
      if want == snailNum :
        snail['want'] = (int((n-1)/2), j)
      snail[(int((n-1)/2), j)] = snailNum 
      snailNum -= 1
  
    #윗면채움
    for i in range(int((n-1)/2)-1,-int((n-1)/2), -1) :
      if want == snailNum :
        snail['want'] = (i, int((n-1)/2))
      snail[(i, int((n-1)/2))] = snailNum 
      snailNum -= 1
  
  return recursive_snail(snail, n-2, want)

snail = {}

snail = recursive_snail(snail,N, want)

for j in range(int((N-1)/2), -int((N-1)/2)-1, -1) :
  for i in range(-int((N-1)/2), int((N-1)/2)+1) :
    if i == int((N-1)/2) :
      print(snail[(i,j)])
    else :
        print(snail[(i,j)], end=' ')
 

print(-snail['want'][1]+ (int((N-1)/2+1)), snail['want'][0] + (int((N-1)/2 +1)))
