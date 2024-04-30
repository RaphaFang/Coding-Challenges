def checkPassword(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    num = '0123456789'
    spe = '!@#$%'

    uppercheck = False
    lowercheck = False
    numcheck = False
    specheck = False

    # Check for each character in the string
    for n in s:
        if n in upper:
            uppercheck = True
        elif n in lower:
            lowercheck = True
        elif n in num:
            numcheck = True
        elif n in spe:
            specheck = True
        else:
            # If character doesn't belong to any allowed categories
            return False

    # Check the length requirement
    lencheck = 8 <= len(s) <= 16

    # Check all conditions
    return uppercheck and lowercheck and numcheck and specheck and lencheck


def checkPassword(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    num='0123456789'
    spe = '!@#$%$'
    
    for n in s:
        if n not in upper and n not in lower and n not in num and n not in spe:
            print("9, False")
            return False
        
    uppercheck = False
    for n in s:
        if upper.find(n)!=-1:
            uppercheck = True
            break

    lowercheck = False
    for n in s:
        if lower.find(n)!=-1:
            lowercheck = True
            break

    numcheck = False
    for n in s:
        if num.find(n)!=-1:
            numcheck = True
            break
    
    specheck = False
    for n in s:
        if spe.find(n)!=-1:
            specheck = True
            break

    lencheck = False
    if len(s)>=8 and len(s)<=16:
        lencheck = True

    if (uppercheck and lowercheck and numcheck and specheck and lencheck)==True:
        return True
    else:
        return False
        
checkPassword("aBcdefg8$")