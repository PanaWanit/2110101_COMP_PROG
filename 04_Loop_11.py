a = input()
a += "/"
c = 1
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        print(a[i-1], c, end=" ")
        c=0
    c+=1
