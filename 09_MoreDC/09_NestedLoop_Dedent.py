n = int(input())

for i in range(n):
    s = input()
    c=0
    for j in range(len(s)):
        if s[j]!='.':
            break
        c+=1
    print(s[c//2:])
