def snail(snail_map):
    len_ll = len(snail_map)
    id_range = len_ll//2

    out_list = []
    for index in range(id_range):  # [2,0]
        up_row = snail_map[index][index:len_ll-index-1]
        out_list+=up_row

        right_row = [i[-index-1] for i in snail_map[index:-index-1]]
        out_list+=right_row

        down_row = snail_map[-index-1][index+1:len_ll-index] # 這要反轉
        out_list+=down_row[::-1]
        
        left_row = [j[index] for j in snail_map[index+1:len_ll-index]] # 這要反轉
        out_list+=left_row[::-1]


    if len_ll%2 == 1:
        dot = len_ll//2
        middle = snail_map[dot][dot]
        out_list.append(middle)

    return (out_list)

    # if len(snail_map)%2 == 0:
    #     len_list = [n*2-1 for n in range(len(snail_map)//2 ,0,-1)]
    # if len(snail_map)%2 == 1:
    #     len_list = [n*2 for n in range(len(snail_map)//2 ,0,-1)] 
    # print(len_list)
            
array = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]

print(snail(array))

# # print(len(array))


aa = [0,1,2,3,4,5]
bb = [3,4,5]
# print(aa[:-1]+bb)  #[0, 1, 2, 3, 4, 5]

# print(bb[-1])

print(aa[1:4])