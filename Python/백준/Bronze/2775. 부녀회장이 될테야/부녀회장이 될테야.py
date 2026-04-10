T = int(input())

def floor(floorlist, k, n) :
  # 만약 0층이면 1, 2, 3 ... n
  if k == 0:
    templist = []
    for i in range(n) :
      templist.append(i+1)
    floorlist.append(templist)
    return floorlist

  floorlist = floor(floorlist, k-1, n)

  templist = []
  #k층의 n개의 방에 맞는 인원수를 구한다.
  for i in range(n) :
    #1번방은 1명.
    if i == 0 :
      templist.append(1)
    else :
      templist.append(templist[i-1] + floorlist[k-1][i])
    
  floorlist.append(templist)
  return floorlist

for i in range(T) :
  k = int(input())
  n = int(input())

  floorlist = []
  floor(floorlist, k, n)
  
  print(floorlist[k][n-1])