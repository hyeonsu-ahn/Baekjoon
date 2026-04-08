N = int(input())

def facto(N) :
  if N <= 1 :
    return 1
  else :
    return N*facto(N-1)

print(facto(N))