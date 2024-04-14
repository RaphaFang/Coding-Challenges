def generateOrdinalNumber(number):
    lis_num = list(str(number))
    try:
        if int(lis_num[-2])==0:
            if int(lis_num[-1])==1:
                return( str(number)+"st")
            if int(lis_num[-1])==2 :
                return( str(number)+"nd")
            if int(lis_num[-1])==3:
                return( str(number)+"rd")
    except IndexError:
        if int(lis_num[-1])==1:
            return( str(number)+"st")
        if int(lis_num[-1])==2 :
            return( str(number)+"nd")
        if int(lis_num[-1])==3:
            return( str(number)+"rd")
    else:
        return( str(number)+"th")

        
    

generateOrdinalNumber(3212)
# 1 對應到 1st
# 2 對應到 2nd
# 3 對應到 3rd
# 4 對應到 4th
# 4 到 19 都可以在後面加上 th 表達序數
# 20 到 100 則以個位數的數字為準，個位數為 0 則使用 th
# 101 以上，則以後面兩位數為準，使用以上規則轉換，例如 101st、311th、1523rd。
    
