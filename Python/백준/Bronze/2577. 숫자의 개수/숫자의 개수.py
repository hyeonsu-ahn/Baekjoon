A = int(input())
B = int(input())
C = int(input())

produc = A*B*C
produc = list(str(produc))


result = {}

for i in range(len(produc)) :
  if produc[i] in result.keys():
    result[produc[i]] += 1
  else :
    result[produc[i]] = 1

for i in range(10) :
  if str(i) in result.keys() :
    print(result[str(i)])
  else :
    print(0)
