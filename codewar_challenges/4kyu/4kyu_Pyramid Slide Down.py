def longest_slide_down(pyramid):
    # ! 這是greedy algorethon ，但是不一定準確，只比較局部資料
    # start_num = 0
    # final = [pyramid[0][0]]
    # print(final)
    # for n in pyramid[1:]:
    #     print(n[start_num], n[start_num+1])
    #     if n[start_num] > n[start_num+1]:
    #         final.append(n[start_num])
    #         start_num +=0
    #     else:
    #         final.append(n[start_num+1])
    #         start_num +=1
    # print(final)

    # return sum(final)

    pyramid.reverse()
    for index, n in enumerate(pyramid[1:]):
        being_add = n
        add_up = pyramid[index]
        # print(being_add)
        # print(add_up)
        # 這步驟的目的是要錯位，透過錯位的資料比較

        for index, k in enumerate(being_add):
            being_add[index] += max(add_up[index], add_up[index+1])
    return (being_add[0])
    # 因為都還在同一個func內，所以都還是local的，不會有local 跨到global
        
test2 = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
test1 = [ 
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            ]
print(longest_slide_down(test1))