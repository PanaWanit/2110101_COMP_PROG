def print_triangle(n):

    print(' '*(n-1)+'*')

    for i in range(n-2):
        print(' '*(n-2-i)+'*' + ' '*(1+2*i) + '*')

    print('*'*(2*n-1))
exec(input())
