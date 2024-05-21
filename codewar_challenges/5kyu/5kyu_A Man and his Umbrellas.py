def min_umbrellas(weather):
    for index,n in enumerate(weather):
        if n =="rainy" or n=='thunderstorms':
            weather[index] = 1
        else:
            weather[index] = 0
    print( weather)

weather = ["overcast", "rainy", "clear", "thunderstorms"]
print(min_umbrellas(weather))



the_0_1 = []