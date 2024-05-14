def bananas(s):
    banana_list = ['b','a','n','a','n','a']

    s_list = list(s)

    if len(s) == 6:
        if "banana" in s:
            return {"banana"}
    if len(s) == 7:
        for n in s_list





    print(s.count('b'))
    print(s.count('a'))
    print(s.count('n'))

    for index , n in enumerate(s):
        print(f'"{n}":{index}')

    # if "banana" in s:
    #      for n in s_list:



print(bananas('bananana'))