def zeros(n):
    count = 0
    power_of_5 = 5
    
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5
    return count

print(zeros(25))

# 大前提機制，數被5除，可以算出這個數列裡面，存在幾個5

# 這邊的n 不會改動，所以先篩選 n 可以被5除
# 如果數夠大，接算被25除，前面用5跑過一次，會抓出25，但是只抓一次，25應該要被抓到兩次，這邊用25找就是補足應該要被找到的第二次