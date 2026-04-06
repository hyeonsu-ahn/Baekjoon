n = list(input())

ps = ""


index = 0
while index < len(n) :
  if index % 10 == 9 :
    ps += n[index]
    print(ps)
    ps = ""
    index += 1
  else :
    ps += n[index]
    index+=1
if index %10 != 0 :
  print(ps)