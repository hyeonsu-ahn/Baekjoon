mushroom = []
for i in range(10) :
  mushroom.append(int(input()))

score = mushroom[0]
stop = 0
for i in range(9) :
  if i != stop :
    break
  if abs(score + mushroom[i+1] - 100) <= abs(score-100) :
    score += mushroom[i+1]
    stop += 1
  
    

print(score) ###

