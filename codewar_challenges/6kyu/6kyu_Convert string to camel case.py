def to_camel_case(text):
    if text != '':
        aaa = ''
        bbb = ''
        # if 
        for n in text.split("_")[1:]:
            # print(n)
            aaa+=n[0].upper() + n[1:]
            # print(aaa)
        aaa = text.split("-")[0]+aaa
        # print(aaa)
        for n in aaa.split("-")[1:]:
            bbb+=n[0].upper() + n[1:]
        bbb = text.split("-")[0]+bbb
        print(bbb)
    return('')


text = 'the_stealth_warrior'

to_camel_case(text)
# ----------------------------------------------------
# n = 'abc'
# n = n[0].upper() + n[1:]
# print(n)