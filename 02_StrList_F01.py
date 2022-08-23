def check_digit(s):
    a = list(map(int, s))
    return (11-sum((13-i)*a[i] for i in range(12))%11)%10

exec(input())
