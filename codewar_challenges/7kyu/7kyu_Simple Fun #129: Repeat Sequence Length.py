def repeat_sequence_len(n):
    def do_the_square(k):
        k_list = [int(s)**2 for s in list(str(k))]
        return sum(k_list)

    the_one = 0
    output_list = [do_the_square(n)]
    for j in range(30):
        now = do_the_square(output_list[j])
        if now in output_list:
            the_one = now
            break
        output_list.append(now)
    return  len(output_list) - output_list.index(the_one)




n1 = 123
print(repeat_sequence_len(n1))


# ll = [0,11,22,333]
# print(ll.index(44))
# ValueError: 44 is not in list
