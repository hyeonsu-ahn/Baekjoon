T = int(input())



for i in range(T) :
  score = 0
  result = 0
  li = list(input())

  for j in range(len(li)) :
    if li[j] == 'O' :
      score += 1
      result += score
    else :
      score = 0
  
  print(result)

