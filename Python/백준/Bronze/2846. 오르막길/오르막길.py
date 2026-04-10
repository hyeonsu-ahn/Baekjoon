N = int(input())

mountain = list(map(int, input().split()))

uphill = []


for i in range(N-1) :
  if i == 0 :
    temphigh = 0
  #내리막이면
  if mountain[i] > mountain[i+1] or mountain[i] == mountain[i+1]:
    uphill.append(temphigh)
    temphigh = 0
  #오르막이면
  elif mountain[i] < mountain[i+1] :
    temphigh += mountain[i+1] - mountain[i]
    if i == N-2 :
      uphill.append(temphigh)
  

print(max(uphill))