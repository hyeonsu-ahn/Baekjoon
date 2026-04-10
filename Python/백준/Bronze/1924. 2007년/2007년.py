month, day = map(int, input().split())

for i in range(1,month +1) :
  target = i
  
  if target == 2 or target ==4 or target ==6 or \
  target ==8 or target ==9 or target ==11 :
    day += 31 

  if target == 3 :
    day += 28 

  if target == 5 or target ==7 or target ==10 or target ==12 :
    day += 30 

  

  


#요일 출력
if day%7 == 1 :
  print("MON")
elif day%7 == 2 :
  print("TUE")
elif day%7 == 3 :
  print("WED")
elif day%7 == 4 :
  print("THU")
elif day%7 == 5 :
  print("FRI")
elif day%7 == 6 :
  print("SAT")
elif day%7 == 0 :
  print("SUN")