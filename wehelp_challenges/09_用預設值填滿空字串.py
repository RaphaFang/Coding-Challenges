def fill(words, value):
    for n in range(len(words)):
        if words[n] == "":
            words[n] = value
    return (words)

    
fill(["Hello", "World", ""], "failed")