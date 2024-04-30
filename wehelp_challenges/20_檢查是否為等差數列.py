def checkArithmeticSequence(nums):
    dif_list = [nums[n+1] - nums[n] for n in range(len(nums)-1)]
    print(dif_list)

    ToF = False
    # for n in range(len(dif_list)-1):
    #     if dif_list[n] == dif_list[n+1]:
    #         ToF=True
    # return ToF
    #!  小錯誤：它只檢查連續兩個差異是否相同，而不是確認所有差異都相同

    for n in dif_list:
        if n != dif_list[0]:
            return False
    return True


checkArithmeticSequence([1,3,6])