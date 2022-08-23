def day_of_year(d, m, y):
    y -= 543

    leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if y%4 == 0 and (y%100 != 0 or y%400 == 0):
        leap[1] = 29
    return(d + sum(leap[i] for i in range(m-1)))

exec(input())
