def suggestKeywords(candidates, prompt):
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    n_list = [(n) for n in candidates if n.startswith(prompt)]
    n_dict = {}
    for n in n_list:
        this_round_n = ''
        for i in n :
            aaa = alp.index(i)+10
            this_round_n += str(aaa)
        n_dict[n] = int(this_round_n)
    
    sorted_dict = dict(sorted(n_dict.items(), key=lambda item: item[1]))
    return (list(sorted_dict.keys()))



def suggestKeywords(candidates, prompt):
    filtered_keywords = [word for word in candidates if word.startswith(prompt)]
    sorted_keywords = sorted(filtered_keywords, key=lambda x: (len(x), x))
    return sorted_keywords

suggestKeywords(["abc", "xyz", "zzz", "ac", "aa"],"a")

# 我的方式也可以運作，但是要將地3行條件設定成 n.startswith(prompt)
# 並且透過lambda 設定讀取長度是更好的方式