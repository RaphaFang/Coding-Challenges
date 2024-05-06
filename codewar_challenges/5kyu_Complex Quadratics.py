def complex_quadratics(eq):
    import re
    print(eq)

    # right = eq[eq.index("=")+1:]
    right = eq.replace("=", "-(") + ")"
    print(right)
    expr = re.sub(r'\-\-', '+', right)  # Handle double negatives
    print(expr)
    expr = re.sub(r'\+\-', '-', expr) 
    print(expr)
    tokens = re.findall(r'[\+\-]?[^+\-]+', expr)
    print(tokens)
    # left = eq[:eq.index("=")]

    # print()
    # print(right[right.index("x^2")-1])

    # split_right = right.split("x^2")
    # print(split_right)


test1 = "x^2+2ix+2=-1"
test2 = "i+ix=x^2+i-ix+2ix^2"
test3 = "(-217+24i)x+1475i+1156=(-20+4i)x-x^2-713i"
complex_quadratics(test3)


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