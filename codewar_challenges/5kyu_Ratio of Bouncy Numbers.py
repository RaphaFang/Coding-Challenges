def bouncy_ratio(ratio):
    going = True
    data = 100000
    total_count = 100
    bouncy_count = 0

    while going:
        for n in range(100,data):
            current_num = list(str(n))
            if (current_num[0]>current_num[1] and current_num[2]>current_num[1]) or (current_num[0]<current_num[1] and current_num[2]<current_num[1]):
                bouncy_count+=1
            total_count+=1
            if bouncy_count/total_count >= ratio:
                print(n)
                print(bouncy_count/total_count)
                break
        going =False

bouncy_ratio(0.5)