def findSecond(nums):
    nums.sort(reverse=True)
    nums = [n for n in nums if n!=nums[0]]
    return nums[0]

findSecond([1, 3, 3, 2, 5, -2]) #>>> 3
findSecond([-5, -10, -8, 1, -1]) #>>> -1
findSecond([0, 2]) #>>> 0
findSecond([-2,1,1,1,0])

# 整理順序，並且倒反
# https://ithelp.ithome.com.tw/articles/10272933
# 刪除最大的數，新list[0]是要return的：似乎沒有可以直接刪除的方式remove()只能刪除一個，pop()要提供index，用comprehension或許比較快
# https://www.51cto.com/article/699740.html