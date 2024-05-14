# D=lambda n:''.join(['+'*n+'\n']+[(' '*(n-k)+'+'*((k*2)-1)+'\n') for k in range(1, n+1)])[:-1]
# D =lambda n: ''.join(['+'*n + '\n'] + [' '*(n-k) + '+'*(2*k-1) + '\n' for k in range(1, n+1)] * 2[::-1])[:-1]
# D = lambda n: ''.join([' ' * (n - k) + '+' * ((k * 2) - 1) + '\n' for k in range(1, n + 1)] + [' ' * (n - k) + '+' * ((k * 2) - 1) + '\n' for k in range(n, 0, -1)])[:-1]
D=lambda n:'+'*n+'\n'+'\n'.join(' '*(n-i)+'+'*(2*i-1)for i in[*range(1,n+1),*range(n,0,-1)])
D=lambda n:'\n'.join(['+'*n]+(s:=[' '*(n-1-k)+'+'*(2*k+1)for k in range(n)])+s[::-1])


print(D(5))

print('A'.join(['aaa']+['bbb']))
# aaaAbbb