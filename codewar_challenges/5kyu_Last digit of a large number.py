def last_digit(n1, n2):
    if n2 == 0:
        return 1
    
    last_digit_a = n1%10

    # Patterns of last digits for bases from 0 to 9
    last_digit_patterns = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }

    cycle = last_digit_patterns[last_digit_a]
    print(cycle)

    cycle_length = len(cycle)
    print(cycle_length)

    effective_index = (n2 - 1) % cycle_length

    return( cycle[effective_index])
    


# last_digit(2,4)
last_digit(2 ** 200, 2 ** 300)
# print((9)**(7))

# ------------------------------------------------------------------------------------------
def last_digit(n1, n2):
    return pow( n1, n2, 10 )

# ------------------------------------------------------------------------------------------

digits = {
    0:[0,0,0,0],   
    1:[1,1,1,1],   
    2:[2,4,8,6],   
    3:[3,9,7,1],   
    4:[4,6,4,6],   
    5:[5,5,5,5],   
    6:[6,6,6,6],   
    7:[7,9,3,1],   
    8:[8,4,2,6], 
    9:[9,1,9,1]
}
def last_digit(n1, n2):
    return digits[n1%10][(n2-1)%4] if n2 else 1
