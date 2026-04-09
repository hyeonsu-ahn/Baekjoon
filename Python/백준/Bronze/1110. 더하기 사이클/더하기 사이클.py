N = list(input())

if len(N) == 1 :
    N.append(N[0])
    N[0] = '0'



def make_num(n) :
  num = []

  num.append(n[1])
  
  x = int(n[0]) + int(n[1])
  x = str(x%10)
  num.append(x)
  
  return num

newnum = make_num(N)
cycle= 1
while newnum != N :
  newnum = make_num(newnum)
  cycle += 1


print(cycle)