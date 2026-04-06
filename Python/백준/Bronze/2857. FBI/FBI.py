A = input()
B = input()
C = input()
D = input()
E = input()
li = [A,B,C,D,E]
count = 0
for i in range(1,6) :
  if count == 0 and li[i-1].count("FBI") :
    print(i, end='')
    count += 1
  elif count != 0 and li[i-1].count("FBI"):
    print(end=' ')
    print(i, end='')
    count+=1
  
    
if count == 0 :
  print("HE GOT AWAY!")