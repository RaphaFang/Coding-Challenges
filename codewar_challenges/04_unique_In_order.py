tur = (1,2,3)
str = "ABCDE"
list1 = [1, 2, 2, 3, 3, 4, 5]


def unique_in_order(sequence):
    for n in list(sequence):
        print(n)
        newlist = []
        if n == n+1:
            print(n + "repeat")
            pass
        else:
            newlist.append(n)
    print(newlist)

# print(list(str))
            
unique_in_order(str)