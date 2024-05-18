def clean_mean(sample, cutoff):
    changes = True
    # current_sample = sample[:]

    while changes:
        mean_num = sum(sample) / len(sample)
        std_dev = (sum((n - mean_num) ** 2 for n in sample) / len(sample)) ** 0.5
        upper = mean_num + std_dev*cutoff
        lower = mean_num - std_dev*cutoff
        print(std_dev)
        # !lower 這邊多打一個負號...搞的下方new_sample的直為空集合

        new_sample = [n for n in sample if n >= lower and n <= upper]
        print(new_sample)

        if len(new_sample) == len(sample):
            changes = False
            new_mean_num = sum(new_sample)/len(new_sample)
        sample = new_sample
        
    return (round(new_mean_num, 2))

        # 這提兩個設計有巧思的地方
        # 1. 原本有設計    # current_sample = sample[:]
            # 但是這不是必要的設計，直接蓋掉舊變數名成就好
        # 2. 檢查離開迴圈的機制，檢查剔除前後長度，若為一樣，則不需再次計算標準差


sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
cutoff = 3
print(clean_mean(sample, cutoff))


# 1. 原本有設計    # current_sample = sample[:]
# list = [0,1,2,3]
# list2= list
# list.append(22)
# print(list2)