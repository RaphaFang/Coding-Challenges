def score(dice):
    score = 0
    three_list =[d for d in dice if dice.count(d)>=3]


    if len(three_list)!=0:
        if three_list[0] == 1:
            score+=three_list[0]*1000
        else:
            score+=three_list[0]*100

    if len(three_list)>3:
        if three_list[3]==1:
            score+=100
        elif three_list[3]==5:
            score+=50

    if len(three_list)>4:
        if three_list[4]==1:
            score+=100
        elif three_list[4]==5:
            score+=50

    for n in dice:
        if (n not in three_list) and n==1:
            score+=100
        if  (n not in three_list) and n==5:
            score+=50
    return(score)



# 這個的時間複雜度反而比第一個很醜的高
# 猜測：下方這寫法有3曾的條件具，而上方的只有2曾。所以直間路雜度上比較快？
    # if three_list:
    #     the_num = three_list[0]
    #     re = dice.count(the_num)

    #     if the_num == 1:
    #         score+=the_num*1000
    #         re-=3
    #     else:
    #         score+=the_num*100
    #         re-=3
    #     while re>0:
    #         if the_num==1:
    #             score+=100
    #             re-=1
    #         if the_num==5:
    #             score+=50
    #             re-=1
    # for n in dice:
    #     if (n not in three_list) and n==1:
    #         score+=100
    #     if  (n not in three_list) and n==5:
    #         score+=50


score([2, 4, 4, 5, 4])

# print(score([2, 4, 4, 5, 4]))

#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point