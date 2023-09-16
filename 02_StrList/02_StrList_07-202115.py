s = input()
a,b = "",""
for i in range(3, 32, 7):
    a += s[i]

for i in range(7, 28, 5):
    b += s[i]

x = int(a) + int(b) + 10000

code = str(x)[-4:-1]
ch = chr(65 + (int(code[0]) + int(code[1]) + int(code[2]))%10)
print(code, ch, sep="")
