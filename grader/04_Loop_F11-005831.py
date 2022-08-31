def RLE(a):
    a += "/"
    l=[]
    c = 1
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            l.append([a[i-1], c])
            c=0
        c+=1
    return l
exec(input())
