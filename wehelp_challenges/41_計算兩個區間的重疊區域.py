def getOverlappingRange(range1, range2):
    f_start ,f_end = range1
    s_start ,s_end = range2
    if (f_start <= s_end and f_end >= s_start):
        aa = max(f_start,s_start)
        bb = min(f_end,s_end)
        return [aa,bb]
    else:
        return []



getOverlappingRange([5, 10],[9, 11])