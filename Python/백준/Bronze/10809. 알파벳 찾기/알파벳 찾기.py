T = list(input())

result = []
for i in range(26):
  result.append(-1)
  for j in range(len(T)):
    if chr(i+97) == T[j]:
      result[i] = j
      break
  
result = list(map(str,result))

print(" ".join(result))



