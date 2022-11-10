a = input().split()
x = list(input())

for opr in x:
    if opr=='C':
        a = a[len(a)//2:]+a[:len(a)//2]
    elif opr=='S':
        a = [a[len(a)//2*(i%2)+i//2] for i in range(len(a))]
print(' '.join(a))

