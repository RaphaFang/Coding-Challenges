def dir_reduc(arr):
    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }

    stack = []
    for direction in arr:
        # If the stack is not empty, and 
        # the last direction in the stack is opposite to the current direction, pop the last direction
        if stack and stack[-1] == opposites[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack
# 前面想說設計兩個迴圈，處理掉 1 2 3 4 ，1 4 相同、2 3 相同的問題
# 但只要用pop()，就可以推掉list中最後一個（如果這時是2），3也不會加進去，下一個審核的回到1




    # print(arr)
    # dict ={'NORTH':arr.count('NORTH'), 'SOUTH':arr.count('SOUTH'), 'WEST':arr.count('WEST'), 'EAST':arr.count('EAST')}
    
    # order = 

    # if dict['NORTH'] ==1 and dict['SOUTH'] ==1 and dict['WEST'] ==1 and dict['EAST'] ==1:
    #     return 


    # if dict['NORTH']>dict['SOUTH']:
    #     dict['NORTH']-=dict['SOUTH']
    #     dict['SOUTH']=0
    # else:
    #     dict['SOUTH']-=dict['NORTH']
    #     dict['NORTH']=0
    # if dict['WEST']>dict['EAST']:
    #     dict['WEST']-=dict['EAST']
    #     dict['EAST']=0
    # else:
    #     dict['EAST']-=dict['WEST']
    #     dict['WEST']=0
    # print(dict)

    # return  [n for n in dict if dict[n] !=0]
    # print(return_list)
    print(arr)
    print(arr[-1])

    # return_list = []
    # for n in range(len(arr)//2):
    #     print(n)
    #     if (arr[n] == "NORTH" and arr[n+1] =="SOUTH") or (arr[n] == "SOUTH" and arr[n+1] =="NORTH"):
    #         pass
    #     elif (arr[n] == "EAST" and arr[n+1] =="WEST") or (arr[n] == "WEST" and arr[n+1] =="EAST"):
    #         pass
    #     else:
    #         return_list.append(arr[n])
    #         return_list.append(arr[n+1])

    #     n+=1
    #     print(n)
    # return_list = return_list #.append(arr[-1])
    # print(return_list)

    # second_return_list = []
    # for n in range(len(arr)-1):
    #     print(n)
    #     if (return_list[n] == "NORTH" and return_list[n+1] =="SOUTH") or (return_list[n] == "SOUTH" and return_list[n+1] =="NORTH"):
    #         pass
    #     elif (return_list[n] == "EAST" and return_list[n+1] =="WEST") or (return_list[n] == "WEST" and return_list[n+1] =="EAST"):
    #         pass
    #     else:
    #         second_return_list.append(arr[n])



    # return []

a = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"]
dir_reduc(a)