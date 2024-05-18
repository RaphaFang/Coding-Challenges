def perimeter(n):
    n_list = [1,1]
    for n in range(2,n+1):
        x = n_list[-1] + n_list[-2]
        n_list.append(x)
    return(sum(n_list)*4)


perimeter(5)


def perimeter(n):
    a, b = 1, 2
    while n:
        a, b, n = b, a + b, n - 1
    return 4 * (b - 1)

