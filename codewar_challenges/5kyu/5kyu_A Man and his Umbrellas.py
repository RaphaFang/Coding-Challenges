def min_umbrellas(weather):
    for index,n in enumerate(weather):
        if n =="rainy" or n=='thunderstorms':
            weather[index] = 1
        else:
            weather[index] = 0
    at_off, at_home = 0, 0
    if weather[0] == 1:
        at_off +=1
    for n in range(1, len(weather)):
        print(weather[n])
        if n%2 == 1 and weather[n] ==1:
            if at_off >=1:
                at_off-=1
                at_home+=1
            else:
                at_home+=1
        if n%2 == 0 and weather[n] ==1:
            if at_home >=1:
                at_home-=1
                at_off+=1
            else:
                at_off+=1
    return at_off + at_home

weather =["rainy"]
print(min_umbrellas(weather))

# first_half = weather[::2]
# second_half = weather[1::2]
# weather_list = list(zip(first_half, second_half))
# print(weather_list)
