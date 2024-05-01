# def isOverlapping(range1, range2):

#     # range1 = (n for n in range(range1[0], range1[1]+1))
#     # range2 = (n for n in range(range2[0], range2[1]+1))
#     # print(range1)
#     # print(range2)
#     ToF = False
#     for n in (n for n in range(range1[0], range1[1]+1)):
#         if n in (n for n in range(range2[0], range2[1]+1)):
#             ToF = True
#             return ToF
#     return ToF


def isOverlapping(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    return ( start1 <= end2 and start2 <= end1)

isOverlapping([5, 10], [9, 11])  # True
isOverlapping([5, 8], [9, 11])  # False
