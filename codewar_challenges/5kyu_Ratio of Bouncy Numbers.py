def bouncy_ratio(ratio):
    going = True
    total_count = 99
    bouncy_count = 0
    start_from_hundreds = 100

    while going: 

        current_num = str(start_from_hundreds)
        is_increasing = True
        is_decreasing = True

        for i in range(len(current_num) - 1):
            if int(current_num[i]) > int(current_num[i + 1]):
                is_increasing = False
            elif int(current_num[i]) < int(current_num[i + 1]):
                is_decreasing = False

        if not is_increasing and not is_decreasing:
            bouncy_count += 1
        total_count += 1
        start_from_hundreds +=1

        if bouncy_count/total_count >=ratio:
            return (total_count)
            print(bouncy_count/total_count)
            break
            # ToF_list = []
            # for i in range(0, len(current_num)-1):
            #     if  (int(current_num[i]) -int(current_num[i+1]) >0):
            #         ToF_list.append(True)
            #     else:
            #         ToF_list.append(False)
            
            # if all(ToF_list) or all(not x for x in ToF_list) == True:
            #     total_count+=1
            # else:
            #     total_count+=1
            #     bouncy_count+=1    
                

        # going =False

bouncy_ratio(0.15)

# # # ToF_list = [False, False]
# # # print(all(ToF_list) or all(not x for x in ToF_list))      # Output: False


# for i in range(0,10):
#     print(i)