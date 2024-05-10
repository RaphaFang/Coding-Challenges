def first_non_repeating_letter(s):
    # 總結：原先寫法，find / index 會算到兩比不同的資料，導致比較時出錯

    # listed_s = list(s)
    # if s:
    #     for n in listed_s:
    #         # lower_n = n.lower()
    #         if s.find(n.lower(),s.index(n.lower())+1) == -1 and s.find(n.upper(),s.index(n.upper())+1) == -1:
    #             print(n)
    # else:
    #     return ''
        
    # Issue Explanation
    # Mixing Case Sensitivity:
    # You're trying to find a non-repeating letter regardless of case sensitivity.
    # But find and index work case-sensitively, leading to incorrect results.
    # Logic Error in find Usage:
    # Your code uses find to search for the character again after its first occurrence (s.find(n.lower(), s.index(n.lower())+1)), but the indexing isn't consistent due to different cases.
    # Loop Logic:
    # The looping structure doesn't differentiate between repeating and non-repeating characters correctly.
    listed_s = list(s)

    if s:
        for n in listed_s:
           print(n)
           if s.lower().count(n.lower()) == 1:
                print( n)
        else:
            print('')

    else:
        print('')


test = 'hello world, eh?'
test2 = 'stress'
test3 = 'sabbccs'
test4 = 'Go hang a salami, I\'m a lasagna hog!'
test5 = 'abba'
first_non_repeating_letter(test5)


for index, n in enumerate(test4):
    print(index, n)

