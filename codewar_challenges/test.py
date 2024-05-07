def complex_quadratics(eq):
    import re
    import cmath

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

   

    # 處理誇號與後方X分離問題
    combine = left+"+"+right

    tokens = re.findall(r'\([^\)]*\)|[+\-]?[^+\-()]+', combine.replace('i', 'j'))
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

    # 處理計算時的空白值問題
    # ['', '(i+1)', '-9'] ['i', '-'] ['-3']
    for n in range(len(new_tokens)):
        if 'x^2' in new_tokens[n]:
            if new_tokens[n][0]=="x":
                new_tokens[n] = "1x^2"
            if new_tokens[n][:2]=="-x":
                new_tokens[n] = "-1x^2"
            if new_tokens[n][:2]=="+x":
                new_tokens[n] = "1x^2"
        elif 'x' in new_tokens[n]:
            if new_tokens[n]=="x":
                new_tokens[n] = "1x"
            if new_tokens[n]=="-x":
                new_tokens[n] = "-1x"
    new_tokens = [n for n in new_tokens if n!="+0"] 
    new_tokens = [n for n in new_tokens if n!="-0"] 
        

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
            elif len(token) ==1:
                x_count.append(token)
            elif token[0] =="(":
                x_count.append(token[:token.index("x")])
            else:
                x_count.append(token[1:token.index("x")])
        else:
            if token[0]=="-" :
                constant_count.append(token)
            elif len(token) ==1:
                constant_count.append(token)
            else:
                constant_count.append(token[1:])

    # ['1x^2', '+ix', '-1x', '(i+1)x^2', '-3', '-9x^2']
    # ['1', '(i+1)', '-9'] ['i', '-1'] ['-3']


    # 透過eval()以及replace('j', '1j')，處理I計算問題
    x2_count = [n.replace('j', '1j')if len(n) == 1 else n for n in x2_count]
    x2_count = [n.replace('j', '1j')if len(n) ==2 and n[0]=="-" else n for n in x2_count]
    a= sum(eval(n) for n in x2_count)
    x_count = [n.replace('j', '1j')if len(n) == 1 else n for n in x_count]
    x_count = [n.replace('j', '1j')if len(n) ==2 and n[0]=="-" else n for n in x_count]
    b= sum(eval(n) for n in x_count)
    constant_count = [n.replace('j', '1j')if len(n) == 1 else n for n in constant_count]
    constant_count = [n.replace('j', '1j')if len(n) ==2 and n[0]=="-" else n for n in constant_count]
    c= sum(eval(n) for n in constant_count)


    # 使用cmath库处理复数运算，提高精度和稳定性
    # first_x = (b*(-1)+(b**2-(4*a*c))**0.5)/2*a
    # seconed_x = (b*(-1)-(b**2-(4*a*c))**0.5)/2*a

    discriminant = cmath.sqrt(b**2 - 4*a*c)
    first_x = (-b + discriminant) / (2 * a)
    seconed_x = (-b - discriminant) / (2 * a)


    # print(first_x)
    # print(seconed_x)

    first_x = f"{first_x.real:.15f} {first_x.imag:+.15f}j"
    # print(first_x)
    seconed_x = f"{seconed_x.real:.15f} {seconed_x.imag:+.15f}j"
    # print(seconed_x)
    print([complex(re.sub(r'\s+', '',first_x)),complex(re.sub(r'\s+', '',seconed_x))])

complex_quadratics('(-217+24i)x+1475i+1156=(-20+4i)x-x^2-713i')