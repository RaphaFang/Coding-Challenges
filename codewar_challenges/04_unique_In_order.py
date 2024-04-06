tur = (1,2,3,4,5,5)
str = "AAABCDE"
list1 = [1, 2, 2, 3, 3, 4, 5, 5]


def unique_in_order(sequence):
    newlist = []
    for n in range(len(list(sequence))):
        print(n)
        try:
            if list(sequence)[n] == list(sequence)[n+1]:
                pass
            else:
                print(list(sequence)[n])
                newlist.append(list(sequence)[n])
        except IndexError:
            if list(sequence)[n] == list(sequence)[n-1]:
                pass
            else:
                newlist.append(list(sequence)[n])
        
    return newlist

unique_in_order(str)