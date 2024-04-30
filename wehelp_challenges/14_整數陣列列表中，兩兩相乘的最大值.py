def findMaxProduct(nums):
    all = []
    for n in range(len(nums)):
        for i in range(len(nums)):
            if n==i:
                pass
            else: 
                all.append(nums[n] * nums[i])
    # print(all)
    return (max(all))

findMaxProduct([3, 1, 9, 4, 5])