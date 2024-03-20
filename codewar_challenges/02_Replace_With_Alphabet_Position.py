# str = "The sunset sets at twelve o' clock."
# print(list(str))



# def alphabet_position(text):
# #     text = "The sunset sets at twelve o' clock."
#     print(list(text))

text =  "The sunset sets at twelve o' clock."
# alphabet_position(text)


# alph_list = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'
# print(alph_list.split(','))

# list(alph_list)

al_list = ['A',' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J', ' K', ' L', ' M', ' N', ' O', ' P', ' Q', ' R', ' S', ' T', ' U', ' V', ' W', ' X', ' Y', ' Z']
# text = "The sunset sets at twelve o' clock."
# x = text.find("'")
bbb = ''
for n in al_list:
    bbb += n
print(bbb)


# aaa = list(text).upper()
# print(aaa)

# -_____________________________
def alphabet_position(text):
    alph_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_list = ['A',' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J', ' K', ' L', ' M', ' N', ' O', ' P', ' Q', ' R', ' S', ' T', ' U', ' V', ' W', ' X', ' Y', ' Z']
    text = text.upper()
    
#     x = text.find("N")
#     print(x)

    for n in list(text):
        print(n)
        if n in alph_list:
            x = text.find(n)
            print(x)
        

# 先列出字母列表 O
# 玄找是否在字母列表裡面
# 是，尋找該自在字母列表的順位
# 否，pass