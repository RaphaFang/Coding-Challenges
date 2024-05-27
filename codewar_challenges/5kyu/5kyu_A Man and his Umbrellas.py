def min_umbrellas(weather):
    for index,n in enumerate(weather):
        if n =="rainy" or n=='thunderstorms':
            weather[index] = 1
        else:
            weather[index] = 0
    if len(weather) == 1 and weather[0] ==1:
        return 1
    if len(weather) == 1 and weather[0] ==0:
        return 0
            
    first_half = weather[::2]
    second_half = weather[1::2]
    weather_list = list(zip(first_half, second_half))
    print(weather_list)


    num, at_off, at_home = 0, False, False

    # 會出問題，因為第一天的統計機制一直有問題
    for n in range(1, len(weather_list)):
        print(n, weather_list[n])
        if weather_list[n-1][1]==0 and weather_list[n][0]==1:
            if at_home == False:
                num +=1
                if weather_list[n][1]==0:
                    at_off == True
                if weather_list[n][1]==1:
                    at_home == True
            else:
                at_home = False

        elif weather_list[n-1]!=(1, 0) and weather_list[n] ==(0,1):
            if at_off == False:
                num +=1
                if weather_list[n]==(0,1):
                    at_home = True
            else:
                at_off = False

    print(f"the 43: {num}")

    if weather_list[0]!=(0,0):
        num +=1
    return num



weather =["cloudy"]
print(min_umbrellas(weather))
