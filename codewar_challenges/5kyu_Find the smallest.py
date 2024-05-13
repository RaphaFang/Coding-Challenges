def smallest(n):
    s = str(n)
    min_number = n  # Start with the original number
    best_i, best_j = 0, 0  # Best indices to move from and to

    # Try moving every digit to every possible position
    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                continue  # No need to move the digit to the same place
            # Create a list of characters
            list_n = list(s)
            # Remove the digit at index i
            digit = list_n.pop(i)
            # Insert the digit at index j
            # ! 這邊list_n.pop，得到的是原先那位置的直
            list_n.insert(j, digit)
            # Convert list back to integer while avoiding leading zeros
            current_number = int(''.join(list_n))
            # Check if the formed number is smaller
            if (current_number < min_number) or (current_number == min_number and i < best_i) or (current_number == min_number and i == best_i and j < best_j):
                min_number = current_number
                best_i, best_j = i, j

    return [min_number, best_i, best_j]


# def smallest(n):
#     list_n =[int(n) for n in  list(str(n))]
#     print(list_n)

#     small = min(list_n[1:])
#     print(f'the smallest: {small}')

#     the_index = len(list_n) - list_n[::-1].index(small) -1
#     print(f'the smallest index: {the_index}')

#     del list_n[the_index]
#     print(list_n)

#     if small>list_n[0]:
#         list_n.insert(1,small)
#         insert_in = 1
#     else:
#         list_n.insert(0,small)
#         insert_in = 0

#     if list_n[0]==0:
#         del list_n[0]
    
#     list_n = [str(n) for n in list_n]

#     if the_index==1 and insert_in==0:
#         the_index=0
#         insert_in=1

#     print (int(''.join(list_n)), the_index, insert_in)

# print(smallest(209917))


# list = [0,1,2,3,4]
# print(list[::-1])



# def smallest(n):
#     list_n =[int(n) for n in  list(str(n))]
#     print(list_n)

#     small = min(list_n[1:])
#     print(f'the smallest: {small}')

#     # the_index = len(list_n) - list_n[::-1].index(small) -1
#     # print(f'the smallest index: {the_index}')

#     the_index_list = [index for index, n in enumerate(list_n) if n ==small]
#     print(the_index_list)
#     # print(f'the smallest index: {the_index_list}')


#     # del list_n[the_index]
#     # print(list_n)

#     the_correct = 0
#     for n in the_index_list:
#         if 


# print(smallest(704786170834894187))


list = [77, 775, 2,0,1,2,3,4,]

print(list.pop(3))