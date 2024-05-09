def generate_hashtag(s):
    if s == '':
        return False

    list = [n for n in s.split(" ") if n!='']
    for n in range(len(list)):
        list[n] = list[n].lower()
        list[n] = list[n][0].upper()+ list[n][1:]
    without_space = "#"+ ''.join(list)

    if len(without_space)>140:
        return False

    print (without_space)


test = 'codewars  is  nice'
test2 = 'c i n'
test3 = 'CoDeWaRs is niCe'
generate_hashtag(test3)

# ------------------------------------------------------------------------

def generate_hashtag(s):
    output = "#"
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output