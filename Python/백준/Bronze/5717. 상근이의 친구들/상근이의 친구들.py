while True :
    li = input().split()
    if li[0] == '0' and li[1] == '0' :
        break
    
    print(int(li[0]) + int(li[1]))
    