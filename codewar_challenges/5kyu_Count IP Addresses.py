def ips_between(start, end):
    start_list = [int(n) for n in start.split(".")]
    print(start_list)
    end_list = [int(n) for n in end.split(".")]
    print(end_list)

    start_num, end_num = 0 , 0
    square=[3,2,1,0]

    for index,n in enumerate(start_list):
        start_num+=n*(256**square[index])
    print(start_num)

    for index,n in enumerate(end_list):
        end_num+=n*(256**square[index])
    print(end_num)


    return(end_num-start_num)

ips_between("10.0.0.0", "10.0.0.50")


# print(256**0)