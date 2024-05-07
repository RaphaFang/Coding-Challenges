def complex_quadratics(eq):
    import re
    print("start = " + eq)

    left = eq[:eq.index("=")]
    right = eq[eq.index("=")+1:]

    
    right = right.replace("+", "A")
    # print(right)
    right = right.replace("-", "+")
    # print(right)
    right = right.replace("A", "-")
    if right[0] ==0:
        pass
    else:
        right = "-"+right

    print(left)
    print(right)

    # 處理誇號與後方X分離問題
    combine = left+"+"+right
    tokens = re.findall(r'\([^\)]*\)|[+\-]?[^+\-()]+', combine)
    print(tokens)
    for n in range(len(tokens)):
        if ")" in tokens[n]:
            tokens[n] = tokens[n]+tokens[n+1]

    # 處理括號分離相加後，重複的X
    new_tokens = []
    new_tokens.append(tokens[0])
    for n in range(1,len(tokens)):
        if ")" in tokens[n-1]:
            pass
        else:
            new_tokens.append(tokens[n])
    print(tokens)

    # 處理計算時的空白值問題
    # ['', '(i+1)', '-9'] ['i', '-'] ['-3']
    for n in range(len(new_tokens)):
        if 'x^2' in new_tokens[n]:
            if new_tokens[n][0]=="x":
                new_tokens[n] = "1x^2"
            if new_tokens[n][:2]=="-x":
                new_tokens[n] = "-1x^2"
        elif 'x' in new_tokens[n]:
            if new_tokens[n]=="x":
                new_tokens[n] = "1x"
            if new_tokens[n]=="-x":
                new_tokens[n] = "-1x"
        
    print(new_tokens)

    # 處理計算次數
    x2_count = []
    x_count = []
    constant_count = []

    for token in new_tokens:
        if 'x^2' in token:
            x2_count.append(token[:token.index("x^2")])
        elif 'x' in token:
            if token[0]=="-":
                x_count.append(token[:token.index("x")])
            else:
                x_count.append(token[1:token.index("x")])
        else:
            if token[0]=="-":
                constant_count.append(token)
            else:
                constant_count.append(token[1:])

    print(x2_count,x_count,constant_count)
    # ['1x^2', '+ix', '-1x', '(i+1)x^2', '-3', '-9x^2']
    # ['1', '(i+1)', '-9'] ['i', '-1'] ['-3']

    

test1 = "x^2+2ix+2=-1"
test2 = "i+ix=x^2+i-ix+2ix^2"
test3 = "(-217+24i)x+1475i+1156=(-20+4i)x-x^2-713i"
test4 = 'x^2+ix-x+(i+1)x^2-3=9x^2'
complex_quadratics(test4)


# 理論上，要先讀^2，加上正負
# 接著X前面的數
# 接著I前面的數



# text = "apple, banana; cherry. date"
# # Replace each delimiter with a comma
# text = text.replace(';', ',').replace('.', ',')
# print(text)
# result = [item.strip() for item in text.split(',')]
# print(result)


# aaa = '10'
# print(aaa.isnumeric())