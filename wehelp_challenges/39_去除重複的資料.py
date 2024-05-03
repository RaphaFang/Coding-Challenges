def removeDuplicates(ns):
    or_list = []
    re_list = []

    for n in ns:
        if ns.count(n) == 1:
            or_list.append(n)
        else:
            if n not in re_list:
                re_list.append(n)
                or_list.append(n)
    return (or_list)


    
removeDuplicates([3, 2, -6, 2, 3, 5, 2])