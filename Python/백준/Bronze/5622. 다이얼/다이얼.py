di = list(input())

num = []

for i in range(len(di)):
    if di[i] == "A" or di[i] == "B" or di[i] == "C" :
      num.append(2)
    elif di[i] == "D" or di[i] == "E" or di[i] == "F" :
      num.append(3)
    elif di[i] == "G" or di[i] == "H" or di[i] == "I" :
      num.append(4)
    elif di[i] == "J" or di[i] == "K" or di[i] == "L" :
      num.append(5)
    elif di[i] == "M" or di[i] == "N" or di[i] == "O" :
      num.append(6)
    elif di[i] == "P" or di[i] == "Q" or di[i] == "R" or di[i] == "S":
      num.append(7)
    elif di[i] == "T" or di[i] == "U" or di[i] == "V" :
      num.append(8)
    elif di[i] == "W" or di[i] == "X" or di[i] == "Y" or di[i] == "Z":
      num.append(9)
    
result = 0

num = [x +1 for x in num]

for i in range(len(num)):
  result += num[i]


print(result)

