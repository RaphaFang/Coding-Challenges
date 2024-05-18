def find_nb(m):
    total = 0
    trying_num = 0

    while total < m:
        trying_num += 1
        total += trying_num**3

#   這個方式確實相較之下需要運算更多次，每次while都要跑一個for loop
#     while total < m:
#         total = 0
#         trying_num+=1
#         for num in range(trying_num):
#             total += (num+1)**3

    if total > m:
        print (-1)
    if total == m:
        print (trying_num)
    
# findNb(1071225) --> 45
# findNb(91716553919377) --> -1
        
find_nb(9796076958746727442)