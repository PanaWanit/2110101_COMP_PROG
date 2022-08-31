from math import *
a,b,c = input().split(",")

tb = 10 ** (len(b))
tc = 10 ** (len(b)+len(c))

numb = int(a+b)
numc = int(a+b+c)

up, dw = numc - numb, tc-tb

gc = gcd(up, dw)

print(up//gc, "/", dw//gc)


