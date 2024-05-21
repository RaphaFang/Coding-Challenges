def min_umbrellas(weather):
    for index,n in enumerate(weather):
        if n =="rainy" or n=='thunderstorms':
            weather[index] = 1
        else:
            weather[index] = 0
    if len(weather) == 1 and weather[0] ==1:
        return 1
    if len(weather) == 1 and weather[0] ==0:
        return 1
            
    first_half = weather[::2]
    second_half = weather[1::2]
    weather_list = list(zip(first_half, second_half))
    print(weather_list)


    # 作法，用list的[1]去比對[0] 
    num=0
    for n in range(1, len(weather_list)):
        print(n, weather_list[n])
        if weather_list[n][0]==1 and weather_list[n-1][1]==0:
            num +=1
        # print(n ==(0,1))
        elif weather_list[n] ==(0,1) and weather_list[n-1]!=(1, 0):
            num +=1
    print(num)

    if weather_list[0]!=(0,0):
        num +=1
    return num



weather = ["cloudy"]
print(min_umbrellas(weather))


# my_list = [1,2,3,4,5,6,7,8,9]
# first_half = my_list[::2]
# second_half = my_list[1::2]
# paired_list = list(zip(first_half, second_half))

# print(paired_list)

# tt= (0,1,2,3,4)
# print(tt[1])