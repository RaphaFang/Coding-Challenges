def solution(roman : str) -> int:
    roma_dict = {'M':1000, 'D': 500, 'C':100, 'L':50,'X':10,'V':5, 'I':1}
    input_list = list(roman)
    input_roman_listed_dict = [{a:roma_dict[a]} for a in roman]
    # print( list(n.keys())[0])
    # [{'M': 1000}, {'M': 1000}, {'M': 1000}, {'C': 100}, {'M': 1000}, {'X': 10}, {'C': 100}, {'I': 1}, {'X': 10}]
    for n in range(len(input_list)-1):
        # print(n)
        if roma_dict[input_list[n]] >= roma_dict[input_list[n+1]]:
            pass
        else:
            input_roman_listed_dict[n][input_list[n]] *= (-1)
    # print(input_roman_listed_dict)
    # [{'M': 1000}, {'M': 1000}, {'M': 1000}, {'C': -100}, {'M': 1000}, {'X': -10}, {'C': 100}, {'I': -1}, {'X': 10}]
    new_list = [list(n.values())[0] for n in input_roman_listed_dict]
    return (sum(new_list))
# 羅馬數字由左至右疊加，但是，如果右邊小位數討到左邊大位數前面，意味著檢法


solution('MMMCMXCIX')


# print( list(Ndict.keys())[0])
# print( list(Ndict.values())[0])
