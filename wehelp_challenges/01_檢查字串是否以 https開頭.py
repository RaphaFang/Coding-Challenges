def checkHTTPS(s):
    
    if "HTTPS://" in s:
        return True
    else:
        return False

s = input().upper()
checkHTTPS(s)

# ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
def checkHTTPS(s):
    if "HTTPS://" in s.upper():
        return True
    else:
        return False

s = ''
checkHTTPS(s)



# startswith(), would be more precise

# https://blog.csdn.net/m0_64896408/article/details/125040914
# ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
def checkHTTPS(s):
    if s.upper().startswith('HTTPS://'):
        return True
    else:
        return False

s = ''
checkHTTPS(s)