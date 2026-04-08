W, H, X, Y, P = map(int, input().split())

r = int(H/2)
players = 0
for i in range(P) :
  x, y = map(int, input().split())
  #W*H 안에있는 플레이어
  if ((X<=x) and (x <= X+W)) and ((Y<=y)and (y<=Y+H)) :
    players += 1
    continue
  #좌측원 안 플레이어 
  if r**2 >= ((X-x)**2 + (Y+r-y)**2) :
    players += 1
    continue
  #우측원 안 플레이어 
  if r**2 >= ((X+W-x)**2 + (Y+r-y)**2) :
    players += 1
    continue


print(players)