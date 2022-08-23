def str2hms(h_str):
    t = h_str.split(":")
    return int(t[0]), int(t[1]), int(t[2])

def hms2str(h, m, s):
    return ('0'+str(h))[-2:]+':'+('0'+str(m))[-2:]+':'+('0'+str(s))[-2:]

def to_sec(h, m, s):
    return h*3600+m*60+s

def to_hms(s):
    return s//3600, s%3600//60, s%60

def diff(h1, m1, s1, h2, m2, s2):
    return to_hms(to_sec(h2, m2, s2) - to_sec(h1, m1, s1))

def main():
    a,b,c = str2hms(input())
    d,e,f = str2hms(input())
    x,y,z = diff(a,b,c,d,e,f)
    print(hms2str(x,y,z))

exec(input())
