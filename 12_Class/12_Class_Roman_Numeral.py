def convert(s):
    ret,i = 0, 0
    s += " "
    while s[i] != " ":
        if s[i] == 'M':
            ret += 1000
            i+=1
        elif s[i] == 'D':
            ret += 500
            i+=1
        elif s[i] == 'L':
            ret += 50
            i+=1
        elif s[i] == 'V':
            ret += 5
            i+=1
        elif s[i] == 'C':
            if s[i+1] == 'M':
                ret += 900
                i += 2
            elif s[i+1] == 'D':
                ret += 400
                i += 2
            else:
                ret += 100
                i += 1
        elif s[i] == 'X':
            if s[i+1] == 'C':
                ret += 90
                i += 2
            elif s[i+1] == 'L':
                ret += 40
                i += 2
            else:
                ret += 10
                i += 1
        elif s[i] == 'I':
            if s[i+1] == 'X':
                ret += 9
                i += 2
            elif s[i+1] == 'V':
                ret += 4
                i += 2
            else:
                ret += 1
                i += 1
    return ret


class roman:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return str(self.r)

    def __add__(self, other):
        ret = int(self) + int(other)
        s=""
        bound = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        while ret != 0:
            for amt, c in bound:
                if ret >= amt:
                    ret -= amt
                    s += c
                    break
        return roman(s)

    def __int__(self):
        return convert(self.r)

    def __lt__(self, rhs):
        return int(self) < int(rhs)
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))
