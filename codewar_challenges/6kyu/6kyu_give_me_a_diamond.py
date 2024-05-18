def diamond(n):
    if n%2 == 0 or n <= 0:
        return None
    if n == 1:
        return '*\n'
    
    dim = "*"
    blank = " "
    next_line = "\n"

    dim_list = [dim + '*'*k for k in range(n)]  # range start from 0, so the *k works
    new_dim_list = [dim_list[i] for i in range(len(dim_list)) if i%2 ==0]
    new_dim_list = [blank*(len(new_dim_list)-j-1) + new_dim_list[j] + next_line for j in range(len(new_dim_list))]
    for m in new_dim_list[len(new_dim_list)-2::-1]:
        new_dim_list.append(m)
    return ("".join(new_dim_list))

diamond(7)



# O:先處理列印出 1 2 3 4 5的list
# O:處理列映出 1 3 5
# O:處理字串前面的空格，以及/n
# O:處理上半部分，下半部分，可以用reverse，或是[1::]
# https://blog.csdn.net/HARDBIRD123/article/details/82261651
# Return null/nil/None/... if the input is an even number or negative,
## 運作方式是，ex, list[3::-1]，先算0 1 2 3 ，再反轉成 3 2 1 0


## original code:
# def diamond(n):
#     if n%2 == 0 or n <= 0:
#         return None
#     if n == 1:
#         return '*\n'
    
#     dim = "*"
#     blank = " "
#     next_line = "\n"

#     dim_list = []
#     for k in range(n):  # got dim
#         dim_list.append(dim)
#         dim += "*"

#     new_dim_list = []
#     for i in range(len(dim_list)):
#         if i%2 !=0:
#             pass
#         else:
#             new_dim_list.append(dim_list[i])

#     for j in range(len(new_dim_list)):
#         new_dim_list[j] = blank*(len(new_dim_list)-j-1) + new_dim_list[j] + next_line

#     for m in new_dim_list[len(new_dim_list)-2::-1]:
#         new_dim_list.append(m)
#     print ("".join(new_dim_list))