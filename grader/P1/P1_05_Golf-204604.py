import math
sum_par, sum_stroke, sum_fixed = 0,0,0
for i in range(9):
    a,b,c = [int(_) for _ in input().split()]
    sum_par += a
    sum_stroke += b
    sum_fixed += min(a+2, b) if c==1 else 0

handicap = math.floor(0.8*(1.5*sum_fixed-sum_par))
print(sum_stroke)
print(handicap)
print(sum_stroke-handicap)


