def count_smileys(arr):
    # time = 0
    # for n in arr:
    #     if (':' in n )or(';' in n):
    #         if ('-' in n ) or ("~" in n) or ("" in n):
    #             if (')' in n )or('D' in n):
    #                 print(n)
    #                 time+=1
    # print (time)
    
    #  ("" in n)，這邊的 '' 會讓任意的資料通過
    time = 0
    for n in arr:
        if (n.startswith(':') or n.startswith(';')) and (n.endswith(')') or n.endswith('D')):
            if len(n) == 3 and (n[1] == '-' or n[1] == '~') or len(n) == 2:
                time+=1
    return time





test1 = [';]', ':[', ';*', ':$', ';-D']
test2 =  [';(', ';D', ';o(', ':oD', ':(', ':oD', ';(', ':o(']
test3 = [':oD', ':(', ';(', ';D', ';D']
test4 =  [':-(', ';-D', ';(', ':D', ':-(', ';oD']
count_smileys(test4)