T = int(input())

for i in range(T):
    H, W, N = input().split()
    if int(W) < 10 :
      W = "0" + W
    
    YY = 1
    XX = 1
    for j in range(int(N) -1) :
      if YY < int(H) :
        YY += 1
      else  :
        YY = 1
        XX += 1
     
    if XX < 10 :
      XX = '0' + str(XX)
    
    print(str(YY) + str(XX))