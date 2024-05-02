def findUnique(ns):
    start_n = ns[0]
    twist_n = 0
    for n in ns:
        if n == start_n:
            pass
        else:
            twist_n = n
            break

    print(twist_n)
    if ns.count(start_n) > ns.count(twist_n):
        return ns.index(twist_n)
    else:
        return ns.index(start_n)

li = [-5, 8, 8, 8]

findUnique(li)