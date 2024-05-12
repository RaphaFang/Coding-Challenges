from itertools import permutations
def next_bigger(n):
    listed_n = [ int(n) for n in list(str(n))]
    listed_n.sort(reverse=True)
    # print(listed_n)

    # all_permutations = permutations(listed_n)
    llist = [int(''.join(str(n)[1:-1].split(', ')))for n in permutations(listed_n)]
    llist.sort()
    print(llist)
    for i in llist:
        if i>n:
            return(i)
    return -1


    # for perm in all_permutations:
    #     # print(''.join(str(perm)))
    #     # print(perm)
    #     for n in perm:
    #         print(n)





#     # gib = ''
#     # for n in listed_n:
#     #     gib+=str(n)
#     # print(gib)
#     # if n == int(gib):
#     #     print -1

next_bigger(12)

# list = [0,1,2,3,4]
# print(list[1:-1])