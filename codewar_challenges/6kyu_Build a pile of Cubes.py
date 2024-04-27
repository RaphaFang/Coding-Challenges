def find_nb(m):
    total = 0
    trying_num = 0

    while total<m:
        total = 0
        trying_num+=1
        for num in range(trying_num):
            total += (num+1)**3
            
    if total > m:
        print (-1)
    if total == m:
        print (trying_num)


# 𝑛3+(𝑛−1)3+(𝑛−2)3+...+13= 𝑚
    
# findNb(1071225) --> 45
# findNb(91716553919377) --> -1
        

        
find_nb(26825883955641)