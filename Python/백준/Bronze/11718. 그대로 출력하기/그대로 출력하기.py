import sys

count = 0
for line in sys.stdin :
    if count > 100 :
        break
    print(line, end='')
    count += 1