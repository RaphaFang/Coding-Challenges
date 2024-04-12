def unique_in_order(sequence):
    if bool(sequence)!=False:
        ori=list(sequence)
        without=list(sequence)[1:]
        output=[]
        output.append(ori[0])
        for n in range(len(without)):
            if without[n]==ori[n]:
                pass
            else:
                output.append(without[n])
        return output
    else:
        return []


unique_in_order('AAAABBBCCDAABBB') #== ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         #== ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   #== [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   #== [1, 2, 3]
unique_in_order([]) #== []

# py切片語法
# https://zhuanlan.zhihu.com/p/79541418

# ------------------------------------------------------------------
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
# ------------------------------------------------------------------
unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]
# ------------------------------------------------------------------
def unique_in_order(iterable):
    return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]
