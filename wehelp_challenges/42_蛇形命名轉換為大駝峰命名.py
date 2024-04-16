def snakeToUpperCamel(name):
    aaa = ''
    for n in name.split("_"):
        aaa += n[0].upper() + n[1:]
    return aaa

snakeToUpperCamel('get_weather_data')


# ----------------------------------------------------
n = 'abc'
n = n[0].upper() + n[1:]
print(n)