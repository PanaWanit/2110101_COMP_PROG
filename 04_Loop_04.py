x = input()
t=""
for i in x:
    if i == '(':
        t+='['
    elif i==')':
        t+=']'
    elif i=='[':
        t += '('
    elif i==']':
        t += ')'
    else:
        t += i
print(t)

