while True :
    li = input()
    if li == "END":
        break
    list(li)
    temp = []
    for i in range(len(li)-1, -1, -1) :
        temp.append(li[i])

    for i in range(len(temp)) :
        print(temp[i], end="")
    print("")
    