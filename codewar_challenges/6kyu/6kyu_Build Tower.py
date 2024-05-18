def tower_builder(n_floors):
    blank = ' '
    star = '*'
    odd_list = [n*2-1 for n in range(1, n_floors+1)]
    print(odd_list)
    star_list = [blank*(n_floors - (n+1)//2) + star*n + blank*(n_floors - (n+1)//2) for n in odd_list]
    return (star_list)

tower_builder(6)

"  *  "
"     *     "
'  ***  '
'  *  '
'  *  '

#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"

['     *     ', '    ***    ', '   *****   ', '  *******  ', ' ********* ', '***********']