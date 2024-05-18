def snail(snail_map):
    if len(snail_map)%2 == 0:
        len_list = [n*2-1 for n in range(len(snail_map)//2 ,0,-1)]
    if len(snail_map)%2 == 1:
        len_list = [n*2 for n in range(len(snail_map)//2 ,0,-1)] +[0]
    print(len_list)

    len = len(snail_map)

    for index,n in enumerate(len_list):  # [2,0]
        up_row = snail_map[index][index:n]
        right_row = [n[-1] for n in snail_map[index:-1]]

        down_row = snail_map[len-1-index][index+1:len-index]
        left_row = [n[0] for n in snail_map[index:-1]]

        # 左跟又有大問題，要調整
            






#     # return snail_map[0]+[snail_map[1][2]]+snail_map[2][::-1]+snail_map[1][:2]

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]

# print(snail(array))

# # print(len(array))


# aa = [0,1,2]
# bb = [3,4,5]
# print(aa[:-1]+bb)  #[0, 1, 2, 3, 4, 5]

# # print(bb[:-1])