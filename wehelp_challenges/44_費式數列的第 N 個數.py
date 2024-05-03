def getFibNumber(n):
    list = [1,1,2]
    for i in range(3,n+1):
        add = list[i-1] + list[i-2]
        list.append(add)
    return(list[n])

    # s2 = 


getFibNumber(9)