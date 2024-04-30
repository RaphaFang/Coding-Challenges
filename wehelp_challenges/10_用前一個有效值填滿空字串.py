def ffill(words):
    for n in range(1, len(words)): # * 跳過[0]
        if words[n] == "":
            words[n] = words[n-1]
            
    return (words)



ffill(["a", "b", "", "c", ""])