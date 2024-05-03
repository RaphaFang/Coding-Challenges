def upperCamelToSnake(name):
    n_list = ''
    for n in name:
        if n.isupper() == True:
            n_list += ("_"+n.lower())

        else:
            n_list += n
            
    return(n_list[1:])

upperCamelToSnake("GetWeatherData")