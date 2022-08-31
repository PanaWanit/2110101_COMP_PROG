s = input()
a = list(map(int, s))
t = (11 - sum((13-i)*a[i] for i in range(12))%11)%10

print(s[0], s[1:5],  s[5:10], s[10:], t)
