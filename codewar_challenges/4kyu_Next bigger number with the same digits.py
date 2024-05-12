from itertools import permutations
def next_bigger(n):
    listed_n = [ int(n) for n in list(str(n))]
    listed_n.sort(reverse=True)
    print(listed_n)

    # all_permutations = permutations(listed_n)
    llist = [int(''.join(str(n)[1:-1].split(', ')))for n in permutations(listed_n)]
    llist.sort()
    print(llist)

    for i in llist:
        if i>n:
            return(i)
    return -1



next_bigger(2017)

# list = [0,1,2,3,4]
# print(list[1:-1])


def next_bigger(n):
    digits = list(str(n))
    length = len(digits)
    
    # Step 1: Identify the pivot
    i = length - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    if i == -1:
        return -1  # No bigger number possible
    
    # Step 2: Find the smallest digit on the right of the pivot that is larger than pivot
    j = length - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Step 3: Swap
    digits[i], digits[j] = digits[j], digits[i]
    
    # Step 4: Reverse the part of the number after the pivot
    digits = digits[:i + 1] + digits[i + 1:][::-1]
    
    return int(''.join(digits))

# Example usage
n = 123
print(next_bigger(n))  