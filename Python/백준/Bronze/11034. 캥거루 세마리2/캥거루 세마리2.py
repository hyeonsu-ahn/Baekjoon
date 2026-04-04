import sys

for line in sys.stdin :
    li = list(map(int, list(line.split())))
    if (abs(li[0] - li[1]) > abs(li[1] - li[2])) :
        print(abs(li[0] - li[1]) -1)
    else :
        print(abs(li[1] - li[2]) -1)
       

