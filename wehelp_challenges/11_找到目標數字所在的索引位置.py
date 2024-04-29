def findIndex(nums, target):
    for n in nums:
        if n == target:
            return( nums.index(n))
    if target not in nums:
        return(-1)

findIndex([3,2,1,5,10], 7)

list = [1,2,3,4,5,6,7,8,9,10]

# print(list.index(10))