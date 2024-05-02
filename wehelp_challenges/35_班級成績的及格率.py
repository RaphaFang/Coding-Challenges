# def getPassRate(grades):
#     if not grades:  # Check if the list is empty
#         return "0%"
#     total = [n for n in grades if n>=60]
#     aaa = len(total)/len(grades) *100
#     bbb = "%.0f" % aaa +'%'
#     print(type(bbb))
#     print(bbb)

# bbb = "%.0f" % aaa +'%'
# ! 這個方式會四捨五入，但是題目要求的是無條件捨去


def getPassRate(grades):
    if not grades:  # Check if the list is empty
        return "0%"
    total = [n for n in grades if n >= 60]
    pass_rate = len(total) / len(grades) * 100
    result = f"{int(pass_rate)}%"
    return( result)

getPassRate([70, 0, 33, 60, 2, 59])