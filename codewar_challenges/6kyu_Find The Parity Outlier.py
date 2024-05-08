def find_outlier(integers):
    new_integers = [n%2 for n in integers]
    general_num = 0
    time = 0
    for n in range(len(new_integers)-1):
        if new_integers[n] == new_integers[n+1] :
            time+=1
        if time >=3:
            general_num = new_integers[n]
            break
    for n in new_integers:
        if n !=general_num:
            aaa = new_integers.index(n)
            break


test1 = [2, 4, 0, 100, 4, 11, 2602, 36] 
test2 = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,35,5,5,5,5,5,5,5,5,5,5,7,7,7,7,1000]; # even at the end

find_outlier(test2)