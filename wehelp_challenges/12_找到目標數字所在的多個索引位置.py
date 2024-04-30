def findIndexes(nums, target):
    num_list = []
    for n in range(len(nums)):
        if nums[n] == target:
            num =  nums.index(target)
            num_list.append(num)
            nums[n] =""
    
    return(num_list)

nums = [-5, 2, -5, 1, -5]
findIndexes(nums, -5)