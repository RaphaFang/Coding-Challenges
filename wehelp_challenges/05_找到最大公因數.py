def findGCD(n1, n2):
    listn1 = [n for n in range(1,n1+1) if n1%n==0]
    listn2 = [n for n in range(1,n2+1) if n2%n==0]
    common_list = [x for x in listn1 if x in listn2]
    return common_list[-1]


findGCD(6,4) #2
findGCD(5,16)#1
findGCD(12,6)#6

# 尋找相同的值：用list cpmprihension
#     common_list = [x for x in listn1 if x in listn2]

# 這是phind上面的：：：

# # Define two lists
# list1 = ['dog', 'turtle', 'elephant', 'slingacademy.com', [1, 2, 3]]
# list2 = ['turtle', 'slingacademy.com', 'giraffe', [1, 2, 3], 'lion']

# # Use a list comprehension to find common elements
# common_list = [x for x in list1 if x in list2]

# # Print the result
# print(common_list)

