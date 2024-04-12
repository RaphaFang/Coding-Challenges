def findLCM(n1, n2):
    list = [n for n in range (max(n1, n2), n1*n2+1) if n%n1==0 and n%n2==0]
    return list[0]

    # listn1 = [n for n in range(1,n1+1) if n1%n==0]
    # listn2 = [n for n in range(1,n2+1) if n2%n==0]
    # common_list = [x for x in listn1 if x in listn2]
    # return common_list[-1]

findLCM(6,4) #12
findLCM(5,16) #80
findLCM(12,6) #12