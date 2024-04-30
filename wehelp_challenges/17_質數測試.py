def checkPrime(n):
    list = [i+1 for i in range(n) if n%(i+1) == 0 ]
    if len(list)==2:
        return (True)
    else:
        return (False)
    # print(list)


checkPrime(2)