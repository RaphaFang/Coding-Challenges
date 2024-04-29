def countWords(s):
    a_list = s.split(" ")
    print(a_list)

    # for n in a_list:
    #     if n == '':
    #         a_list.remove('')
    # 這個方式會導致一邊移除一邊pharse，會出問題移不乾淨


    a_list = [n for n in a_list if n!='']
    # list compre 則不會發生這問題

    # print(a_list)
    return(len(a_list))

countWords("    ")
