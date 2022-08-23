from math import *

def leap_year(y):
    return True if y%4==0 and (y%100!=0 or y%400==0) else False

def day_til_eof(d, m, y):
    m_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(y)==True:
        m_d[1] = 29
    return (m_d[m-1]-d+1) + sum(m_d[i] for i in range(m, 12))

def day_til_now(d, m, y):
    m_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(y)==True:
        m_d[1] = 29
    return d+sum(m_d[i] for i in range(m-1))-1

bd, bm, by, d, m, y = map(int, input().split())

by -= 543
y -= 543

s = day_til_eof(bd, bm, by) + (y-by-1)*365 + day_til_now(d, m, y)

print( "%d %.2f %.2f %.2f" % (s, sin(2*pi*s/23), sin(2*pi*s/28), sin(2*pi*s/33)) )


