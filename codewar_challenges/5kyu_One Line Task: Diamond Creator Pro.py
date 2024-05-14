D=lambda n:''.join(['+'*n+'\n']+[(' '*(n-k)+'+'*((k*2)-1)+'\n') for k in range(1, n+1)])[:-1]
# D =lambda n: ''.join(['+'*n + '\n'] + [' '*(n-k) + '+'*(2*k-1) + '\n' for k in range(1, n+1)] * 2[::-1])[:-1]
# D = lambda n: ''.join([' ' * (n - k) + '+' * ((k * 2) - 1) + '\n' for k in range(1, n + 1)] + [' ' * (n - k) + '+' * ((k * 2) - 1) + '\n' for k in range(n, 0, -1)])[:-1]
D=lambda n:'+'*n+'\n'+'\n'.join(' '*(n-i)+'+'*(2*i-1)for i in[*range(n+1),*range(n,0,-1)])

def diamond(n):
    if n%2 == 0 or n <= 0:
        return None
    if n == 1:
        return '*\n'
    
    dim = "*"
    blank = " "
    next_line = "\n"

    dim_list = [dim + '*'*k for k in range(n)]  # range start from 0, so the *k works
    new_dim_list = [dim_list[i] for i in range(len(dim_list)) if i%2 ==0]
    new_dim_list = [blank*(len(new_dim_list)-j-1) + new_dim_list[j] + next_line for j in range(len(new_dim_list))]
    for m in new_dim_list[len(new_dim_list)-2::-1]:
        new_dim_list.append(m)
    return ("".join(new_dim_list))

# diamond(7)

# D(3)
a='''\
+++
  +
 +++
+++++
+++++
 +++
  +'''
b='''\
+++++
    +
   +++
  +++++
 +++++++
+++++++++
+++++++++
 +++++++
  +++++
   +++
    +'''

print(D(5))

# '+++\n  +\n +++\n+++++\n+++++\n +++\n  +\n'
# '+++\n  +\n +++\n+++++\n+++++\n +++\n  +'

# '+++++\n    +\n   +++\n  +++++\n +++++++\n+++++++++\n+++++++++\n +++++++\n  +++++\n   +++\n    +\n'
# '+++++\n    +\n   +++\n  +++++\n +++++++\n+++++++++\n+++++++++\n +++++++\n  +++++\n   +++\n    +'


# word = 'abcde'

# print(word[:-2])

'+++\n  +\n +++\n+++++\n +++\n  +'
'+++\n  +\n +++\n+++++\n+++++\n +++\n  +'