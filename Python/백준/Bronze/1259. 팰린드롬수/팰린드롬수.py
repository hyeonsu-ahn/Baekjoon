while True :
  pelindrom = list(input())
  if pelindrom[0] == '0' :
    break
  templist = []

  for i in range(len(pelindrom)-1, -1, -1) :
    templist.append(pelindrom[i])
  
  if templist == pelindrom :
    print('yes')
  else :
    print('no')