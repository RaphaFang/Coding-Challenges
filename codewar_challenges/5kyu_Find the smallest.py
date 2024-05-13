def smallest(n):
    list_n =[int(n) for n in  list(str(n))]
    print(list_n)

    small = min(list_n[1:])
    print(small)

    the_index = list_n.index(small)
    del list_n[the_index]
    print(list_n)

    if small>list_n[0]:
        list_n.insert(1,small)
        insert_in = 1
    else:
        list_n.insert(0,small)
        insert_in = 0

    if list_n[0]==0:
        del list_n[0]

    
    list_n = [str(n) for n in list_n]
    # print(list_n)

    if the_index==1 and insert_in==0:
        the_index=0
        insert_in=1


    return (int(''.join(list_n)), the_index, insert_in)



print(smallest(199819884756))