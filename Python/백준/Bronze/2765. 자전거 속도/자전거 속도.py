import math
N = 0

while True :
    inchradian, rpm, tiPs = map(float, input().split())
    N += 1
    if rpm == 0 :
        break
    
    mileradian = inchradian / (12.0 * 5280.0)
   
    distance = mileradian* 3.1415927 * rpm
    
    tiPh = tiPs / (3600.0)
    
    mph = distance / tiPh
    
    print("Trip #" + str(N) + ":", "{:.2f}".format(distance), "{:.2f}".format(mph) )