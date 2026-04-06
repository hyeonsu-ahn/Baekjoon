N = int(input())
sizeOfline = 2*N - 1
star = 2*N-1
front = 1
for i in range(1, 2*N -1) :
  if(front == 1) :
    for j in range(int((sizeOfline - star)/2)) :
      print(end=" ")
    for j in range(star,0, -1) :
      print(end='*')
    print()
    if(star == 1) and (front == 1) :
      front = 0
    elif (star != 1) and (front == 1) :
      star -= 2

  if(front == 0) :
    star += 2
    for j in range(int((sizeOfline - star)/2)) :
      print(end=" ")
    for j in range(star,0, -1) :
      print(end='*')
    if(star != sizeOfline) :
      print()

if(N == 1) :
  print('*')
    

