a = list(map(float, input().split()))
s = a[0] + a[1] + a[2] + a[3] - max(a) - min(a)
print(round(s/2, 2))
