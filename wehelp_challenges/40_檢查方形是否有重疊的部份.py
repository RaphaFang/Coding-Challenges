# def isOverlapping(rect1, rect2):
#     f_x_start, f_x_end = rect1[0], rect1[0]+rect1[2]
#     f_y_start, f_y_end = rect1[1], rect1[1]-rect1[3]

#     s_x_start, s_x_end = rect2[0], rect2[0]+rect2[2]
#     s_y_start, s_y_end = rect2[1], rect2[1]-rect2[3]

#     if (f_x_start <= s_x_end and f_x_end >= s_x_start) or (f_y_start <= s_y_end and f_y_end >= s_y_start):
#         return(True)
#     else:
#         return(False)

def isOverlapping(rect1, rect2):
    f_x_start, f_x_end = rect1[0], rect1[0] + rect1[2]
    f_y_start, f_y_end = rect1[1], rect1[1] - rect1[3]

    s_x_start, s_x_end = rect2[0], rect2[0] + rect2[2]
    s_y_start, s_y_end = rect2[1], rect2[1] - rect2[3]

    if (f_x_start <= s_x_end and f_x_end >= s_x_start) and (f_y_start >= s_y_end and f_y_end <= s_y_start):
        return True
    else:
        return False

test1= [0, 0, 10, 10],[-5, 5, 5, 5]
test2=([10, 0, 10, 5],[30, 5, 10, 5])
isOverlapping([0, 0, 10, 10],[-5, 5, 5, 5])