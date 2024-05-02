def comparePokerCard(c1, c2):
    order = ['2','3','4','5','6','7','8','9','10','J', "Q", 'K',"A"]
    big = ['C','D','H','S']

    # last = c1[1::-1].reverse()
    # # c1.pop(last)
    print(len(c1))

    # print(last)

    if len(c1) >2:
        c1_order = order.index(c1[0]+c1[1])
    else:
        c1_order = order.index(c1[0])
    if len(c2) >2:
        c2_order = order.index(c2[0]+c2[1])
    else:
        c2_order = order.index(c2[0])

    print(c1_order, c2_order)

    if c1_order > c2_order:
        return(True)
    elif c1_order == c2_order:
        if big.index(c1[-1]) > big.index(c2[-1]):
            return (True)
        else:
            return( False)
    else:
        return( False)

comparePokerCard("KC","3H")