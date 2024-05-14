# def bananas(s):
    # banana_list = ['b','a','n','a','n','a']

    # s_list = list(s)

    # if len(s) == 6:
    #     if "banana" in s:
    #         return {"banana"}
        
    # if len(s) >= 7:
    #     seven_list = []
    #     for index, n in enumerate(s_list):
    #         dul_s_list = s_list[:]
    #         dul_s_list[index] ='-'
            
    #         if len(s) == 8:
    #             eight_list = []
    #             for index, n in enumerate(seven_list):
    #                 dul_s_list = seven_list[:]

    #                 dul_s_list[index] ='-'
    #                 eight_list.append(dul_s_list)
    #             print(eight_list)


    #         seven_list.append(dul_s_list)
    #     print(seven_list)


    #     for n in seven_list:
    #         n







    # print(s.count('b'))
    # print(s.count('a'))
    # print(s.count('n'))

    # for index , n in enumerate(s):
    #     print(f'"{n}":{index}')

    # if "banana" in s:
    #      for n in s_list:
            
def find_bananas(s):
    target = "banana"
    results = []
    
    def recurse(subseq, idx, path):
        if idx == len(target):  # If we have completed the word "banana"
            results.append("".join(path))  # Join the path into a string and add to results
            return
        # Find the next occurrence of target[idx] in subseq
        for i in range(len(subseq)):
            if subseq[i] == target[idx]:
                # Construct the new path including '-' for skipped characters
                new_path = path + ['-' * i + target[idx]]
                # Continue with the remaining part of subseq and target
                recurse(subseq[i+1:], idx + 1, new_path)
    
    recurse(s, 0, [])
    
    # Process results to match the required output format: concatenate all segments into one string
    processed_results = [''.join(result) + '-' * (len(s) - len(''.join(result))) for result in results]
    return processed_results



print(find_bananas('bananaa'))