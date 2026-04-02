import sys
end = False

while not end:
  a, b = map(int, sys.stdin.readline().split()) 
  if a == 0 and b == 0:
    end = True
  else:
   print(a+b)

