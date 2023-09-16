s = input()

def rot13(s):
    if not s.isalpha():
        return s
    shf = ord('A' if 'A' <= s <= 'Z' else 'a')
    num = ord(s)-shf
    num = (num+13)%26
    return chr(num+shf)
while s!='end':
    print(''.join([rot13(c) for c in s]))
    s = input()
