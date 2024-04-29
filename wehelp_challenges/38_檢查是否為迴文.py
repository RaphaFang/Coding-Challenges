def checkPalindrome(s):
    aaa = list(s)
    aaa.reverse()
    reverse_s = ("".join(aaa))

    num = 0 
    for n in range(len(s)):
        if s[n] == reverse_s[n]:
            num+=1
    if num == len(s):
        return(True)
    else:
        return(False)



checkPalindrome("abccba")