x = int(input())
a=[]
while x!=1:
    a.append(str(x))
    if x%2==0:
        x=x//2
    else:
        x = x*3+1
a.append('1')
print('->'.join(a[-15:]))
