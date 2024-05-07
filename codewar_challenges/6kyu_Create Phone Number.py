# def create_phone_number(n):
#     # for i in n:
#     #     print(i)
#     return( f'({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}')

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


# def create_phone_number(n):
# 	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)



# print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# # 通过字典设置参数
# site = {"name": "菜鸟教程", "url": "www.runoob.com"}
# print("网站名：{name}, 地址 {url}".format(**site))
 
# # 通过列表索引设置参数
## my_list = ['菜鸟教程', 'www.runoob.com']
## print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的


def sum_complex(lists):
    total = 0
    for lst in lists:
        for item in lst:
            # 将字符串中的 i 替换为 j（Python中的虚数单位）
            item = item.replace('i', 'j')
            # 使用 eval() 来计算字符串表达式的值
            total += eval(item)
    return total

# 定义三个列表，其中包含复数和实数
a = ['1', '(1+1j)', '-9']
b = ['+1j', '-1']
c = ['-3']

# 计算三个列表的数值总和
result = sum_complex([a, b, c])
print("Sum of all values:", result)

print(type(result))