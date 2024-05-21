def find_all(sum_dig, digs):
    def generate_numbers_with_sum(sum_dig, digs, current_num="", current_sum=0):
        if len(current_num) == digs:
            if current_sum == sum_dig:
                yield int(current_num)
            return

        start_digit = int(current_num[-1]) if current_num else 1
        for digit in range(start_digit, 10):
            if current_sum + digit + (digs - len(current_num) - 1) * 9 < sum_dig:
                continue
            if current_sum + digit + (digs - len(current_num) - 1) * 1 > sum_dig:
                break
            yield from generate_numbers_with_sum(sum_dig, digs, current_num + str(digit), current_sum + digit)

    final = list(generate_numbers_with_sum(sum_dig, digs))
    
    if not final:
        return []

    return [len(final), min(final), max(final)]


# —————————————————————————————————————————————————————————————————————————
    # def is_ascending(num):
    #     num_str = str(num)
    #     for i in range(len(num_str) - 1):
    #         if num_str[i] > num_str[i + 1]:
    #             return False
    #     return True

    # #  條件二：digs個位數
    # # three_digs_list =(o for o in range(10**(digs-1),10**digs) if is_ascending(o))

    # #  條件一：加起來要是sum_dig
    # # llist = []
    # # for n in (o for o in range(10**(digs-1),10**digs) if is_ascending(o)):
    # #     n_list = list(str(n))
    # #     if sum(int(n) for n in n_list) == sum_dig:
    # #         llist.append(n)

    # llist = [n for n in (o for o in range(10**(digs-1),10**digs) if is_ascending(o)) if sum(int(n) for n in list(str(n))) == sum_dig]

    # if not llist:
    #     return []
    # return [len(llist), min(llist), max(llist)]
# —————————————————————————————————————————————————————————————————————————
    #  ! 這應該是我可以做出來的最佳解了，透過兩個func，以及山檢調一半時間複雜度的數值
    def is_ascending(num):
        num_str = str(num)
        for i in range(len(num_str) - 1):
            if num_str[i] > num_str[i + 1]:
                return False
        return True
    
    def the_correct_sum(num):
        n_list = list(str(num))
        if sum(int(n) for n in n_list) == sum_dig:
            return True
        return False
    
    if sum_dig//digs >=10:
        return []

    end = ((sum_dig//digs)+1)*(10**(digs-1))
    print(end)
    start = 10**(digs-1)
    print(start)

    llist = [n for n in (k for k in range(10**(digs-1),end) if the_correct_sum(k)) if is_ascending(n)]
    if not llist:
        return []
    return [len(llist), min(llist), max(llist)]
# —————————————————————————————————————————————————————————————————————————


print(find_all(10, 3))


# kkk = [91,92,93]
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