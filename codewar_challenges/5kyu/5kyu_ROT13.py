def rot13(message):
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message_list = list(message)

    for n in range(len(message_list)):
        if message_list[n].lower() in alp:
            if message_list[n].isupper():
                find_n = alp.index(message_list[n].lower())
                message_list[n] = alp[find_n+13].upper()
                print(message_list[n] )
            else:
                find_n = alp.index(message_list[n].lower())
                message_list[n] = alp[find_n+13]

    print(message_list)

    return ''.join(message_list)
    
re_test = 'Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)'
test = 'ROT13 example'
rot13(re_test)

#-----------------------------------------------------------------------
import string

def rot13(message):
    first = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    trance = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    return message.translate(string.maketrans(first, trance))  