# def power_mod(x, y, n):
#     aa = (x**y)%n
#     return aa

def power_mod(x, y, n):
    result = 1
    base = x % n
    
    while y > 0:
        if y % 2 == 1:  # 如果 y 是奇数
            result = (result * base) % n
        base = (base * base) % n  # 将 base 平方
        y //= 2  # 将 y 右移一位
    
    return result
