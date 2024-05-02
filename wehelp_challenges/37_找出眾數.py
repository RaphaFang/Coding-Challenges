def findMode(ns):
    max_num = 1
    num = 0
    for n in ns:
        big_num = ns.count(n)
        
        if big_num> max_num:
            max_num = big_num
            num = n
    return (num)
        # max_num = max(max_num , big_num)
            
findMode([6, 0, 8, 8, 10])
