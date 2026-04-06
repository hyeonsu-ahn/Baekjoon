T = list(input().upper())

mostusedword = 0
result = ''
for j in range(26) :
    if mostusedword < T.count(chr(j+65)) :
      mostusedword = T.count(chr(j+65))
      result = chr(j+65)
   
for j in range(26) :
    if mostusedword == T.count(chr(j+65)) and result != chr(j+65):
      result = "?"
    

print(result)
