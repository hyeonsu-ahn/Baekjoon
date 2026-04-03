li = []

for i in range(9) :
    li.append(int(input()))

maxNum = max(li)

maxindex = li.index(maxNum)
print(maxNum)
print(maxindex+1)