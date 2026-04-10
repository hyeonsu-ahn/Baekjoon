stringcube = []

for i in range(5) :
  stringcube.append(list(input()))

result = ''

maxlen = len(stringcube[0])

for i in range(1,5) :
  if maxlen < len(stringcube[i]) :
    maxlen = len(stringcube[i])

for i in range(maxlen) :
  for j in range(5):
    try :
      result += stringcube[j][i]
    except IndexError:
      continue



print(result)