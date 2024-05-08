def domain_name(url):
    if "//www." in url:
        start = url.find('//www.')+6
    elif "//" in url:
        start = url.find('//')+2
        # print(url[start:])
    elif "www." in url:
        start = url.find('www.')+4
    else:
        start = 0
    print(url[start:])
    if "." in url:
        end = url[start:].find('.')
    return (url[start:][:end])
    

test = 'http://github.com/carbonfive/raygun'
test2 = 'http://www.codewars.com/kata/'
test3 = 'icann.org'
test4 = 'www.xakep.ru'
domain_name(test4)




def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
# 這應該是最聰明的答案