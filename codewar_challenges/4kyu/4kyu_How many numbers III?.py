def find_all(sum_dig, digs):

    def is_ascending(num):
        num_str = str(num)
        for i in range(len(num_str) - 1):
            if num_str[i] > num_str[i + 1]:
                return False
        return True

    #  條件二：digs個位數
    three_digs_list = range(10**(digs-1),10**digs)

    #  條件一：加起來要是sum_dig
    llist = []
    for n in three_digs_list:
        n_list = list(str(n))
        if sum(int(n) for n in n_list) == sum_dig:
            llist.append(n)
    print(llist)

    final = []
    for n in llist:
        if is_ascending(n):
            final.append(n)
    return([len(final), min(final),max(final)])


    # #  條件三：由小到大
    # for k in llist:
    #     for j in range(0,len(k) - 1):
    #         if k[j]> k[j+1]:
    #             break
    #         else:
    #             final.append(int(''.join(k)))

    # print(final)
    # return([len(final), min(final),max(final)])






print(find_all(35, 6))


kkk = [91,92,93]
# print(sum(kkk))

# kk = 999
# # print(sum(
# #     list(str(kk)))
# #     )
# kk = sum(int(n) for n in str(kk))
# print(kk)
# print(kkk[:-1])

# index,n in enumerate(n_list[:-1])
# n_list[index]