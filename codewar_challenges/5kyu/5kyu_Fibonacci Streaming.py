# def all_fibonacci_numbers(n):
#     start = [1,1]
#     for i in range(2,n):
#         sum_num = start[i-1] + start[i-2]
#         start.append(sum_num)
#         if len(start)==n:
#             return start
        
def all_fibonacci_numbers():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

    
print(all_fibonacci_numbers())

# 我寫的可以運作，但是題目要求的是一個不斷丟出


# https://blog.csdn.net/mieleizhi0522/article/details/82142856
# aa =  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
# print(len(aa))

def foo():
    print("start...")
    while True:
        throw = yield 10
        print("throw:",throw)
g = foo()
print(next(g))
print("*"*20)
print(next(g))