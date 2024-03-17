def findMax(nums):
    max = nums[0]
    for _ in nums:
        if  _ > max:
            max = _
    return max
        
nums = [0]
# nums = []
findMax(nums)