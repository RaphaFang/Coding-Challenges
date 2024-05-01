def findMaxZero(nums):
    con = 0
    for n in range(len(nums)-1):
        # print(nums[n])
        if nums[n] == nums[n+1] and nums[n] ==0:
            con +=1

    if con !=0:
        con+=1

    if len(nums)==1 and nums[0]==0:
        con+=1

    print (con)



findMaxZero([0,0,1,0,0])



# test = [1,2,3,4,5, 5]

# # print(type(int(test[0::-1])))
# print(max(test))