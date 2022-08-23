def leap_year(y):
    return True if y%4==0 and (y%100!=0 or y%400 == 0) else False

d,m,y = map(int, input().split())

d += 15

n=31

if m in [4, 6, 9, 11]:
    n = 30
if m==2:
    n = 29 if leap_year(y-543) else 28

if d > n:
    d-=n
    m+=1
    if m > 12:
        m = 1
        y+=1

print(d, m, y, sep="/")

