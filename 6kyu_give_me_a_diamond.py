def diamond(n):
    dim = "*"
    dim_list=[]

    for k in range(n):  # got dim
        dim_list.append(dim)
        dim += "*"
    
    print(len(dim_list))

    for i in range(len(dim_list)):
        new_dim_list = []
        if i%2 ==0:
            pass
        else:
            new_dim_list.append(dim_list[i])
    print(new_dim_list)   


    # print(dim_list)

    # for s

diamond(5)

# "  *\n ***\n*****\n ***\n  *\n"


# O:先處理列印出 1 2 3 4 5的list
# 處理列映出 1 3 5
# 處理字串前面的空格，以及/n
# 處理上半部分，下半部分，可以用reverse，或是[1::]
