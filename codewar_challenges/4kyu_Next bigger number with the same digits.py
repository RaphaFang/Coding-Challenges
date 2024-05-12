from itertools import permutations


def next_bigger(n):
    listed_n = [ int(n) for n in list(str(n))]
    # listed_n.sort(reverse=True)
    print(listed_n)

    all_permutations = permutations(listed_n)

    llist = [''.join(str(n)) for n in all_permutations]

    print(llist)

    # for perm in all_permutations:
    #     # print(''.join(str(perm)))
    #     # print(perm)
    #     for n in perm:
    #         print(n)





    # gib = ''
    # for n in listed_n:
    #     gib+=str(n)
    # print(gib)
    # if n == int(gib):
    #     return -1

next_bigger(2017)