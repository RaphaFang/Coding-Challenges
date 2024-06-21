# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    aa = list(s)
    bb = []
    for k in aa:
        if k not in bb:
            bb.append(k)
    freqs = [(n,aa.count(n)) for n in bb]
    return freqs

# # takes: [ (str, int) ], str; returns: String (with "0" and "1")
# def encode(freqs, s):

#     return ""
  
# # takes [ [str, int] ], str (with "0" and "1"); returns: str
# def decode(freqs,bits):
#     return ""
# aaaabbbccde aaaabcc
the_para = frequencies('aaaabbbccde')
the_para.sort(key=lambda x: x[1])
print(the_para)

the_len = len(the_para)
dd_dict = {}
starting =''
if the_len > 1:
    for index,n in enumerate(the_para[::-1]):
        tempo_num = 0
        for k in the_para[0:the_len-index-1]:
            tempo_num += k[1]
        if tempo_num!=0:
            if tempo_num >= n[1]:
                starting += '0' 
                dd_dict[n[0]]=starting
                starting = starting[:-1]+'1'
            else:
                starting += '1'
                dd_dict[n[0]]=starting
                starting = starting[:-1]+'0'
        else:
            dd_dict[n[0]]=starting

print(dd_dict)
print('----')
