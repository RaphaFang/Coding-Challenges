num = 51

def descending_order(num):
    num_list = [int(i) for i in str(num)]
    aaa = ''
    for n in sorted(num_list, reverse=True):
        aaa += str(n)
    return int(aaa)

descending_order(num)

# ___________________________________________________
# even better solution
def descending_order(num):
    return int("".join(sorted([num for num in str(num)], reverse=True)))

# ___________________________________________________
# or this
def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)