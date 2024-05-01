def findMaxZero(nums):
    max_consecutive_zeros = 0
    current_zeros = 0

    for num in nums:
        if num == 0:
            current_zeros += 1
            max_consecutive_zeros = max(max_consecutive_zeros, current_zeros)
            # max 這裡max比較（）中的兩個input或是多個，推出去最大的值
            # 如果遇到1，導致脫離loop，current_zeros會規零，但是max_consecutive_zeros不會
            # 仍會透過max()中的 max_consecutive_zeros，確保最大值的紀錄
        else:
            current_zeros = 0  # Reset the zero counter when a 1 is encountered
    return( max_consecutive_zeros)

# def findMaxZero(nums):
#     con = 0
#     li = []

#     if len(nums)==1 and nums[0]==0:
#         print (1)
#     else:
#         for n in range(len(nums)-1):
#             if nums[n] == nums[n+1] and nums[n]==0:
#                 con +=1
#             else:
#                 con+=1
#                 li.append(con)
#                 con=0
#         li.append(con)
#     print(li)



findMaxZero([0,0,0,1,0])