mname = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def read_date():
    x = input().split()
    return [int(x[0]), int(mname.index(x[1]))+1, int(x[2])]
def zodiac(d, m):
    z1=""
    if d >= 22 and m==3 or d <=21 and m==4 : z1 = "Aries"
    elif d >= 22 and m==4 or d <=21 and m==5 : z1 = "Taurus"
    elif d >= 22 and m==5 or d <=21 and m==6 : z1 = "Gemini"
    elif d >= 22 and m==6 or d <=21 and m==7 : z1 = "Cancer"
    elif d >= 22 and m==7 or d <=21 and m==8 : z1 = "Leo"
    elif d >= 22 and m==8 or d <=21 and m==9 : z1 = "Virgo"
    elif d >= 22 and m==9 or d <=21 and m==10 : z1 = "Libra"
    elif d >= 22 and m==10 or d <=21 and m==11 : z1 = "Scorpio"
    elif d >= 22 and m==11 or d <=21 and m==12 : z1 = "Sagittarius"
    elif d >= 22 and m==12 or d <=20 and m==1 : z1 = "Capricorn"
    elif d >= 21 and m==1 or d <=20 and m==2 : z1 = "Aquarius"
    elif d >= 21 and m==2 or d <=21 and m==3 : z1 = "Pisces"
    return z1
def days_in_feb(y):
    return 29 if y%4==0 and (y%100!=0 or y%400==0) else 28
def days_in_month(m, y):
    dim = [31, days_in_feb(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dim[m-1]

def days_in_between(d1, m1, y1, d2, m2, y2):
    if [y2, m2, d2] < [y1, m1, d1]:
        y1, m1, d1, y2, m2, d2 = y2, m2, d2, y1, m1, d1

    dim = [31, days_in_feb(y1), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dim2 = [31, days_in_feb(y2), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    til2 = (sum(dim2[i] for i in range(m2-1))+d2)
    btw = int((y2-y1-1)*365.25)
    til_end1 = (sum(x for x in dim))-(sum(dim[i] for i in range(m1-1))+d1)
    return til2+btw+til_end1

def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))

exec(input().strip())
