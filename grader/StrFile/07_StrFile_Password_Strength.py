def less_than_8_char(s):
    return len(s) < 8

def no_lower_case(s):
    return not any(c.islower() for c in s)

def no_upper_case(s):
    return not any(c.isupper() for c in s)

def no_num(s):
    return not any(c.isdigit() for c in s)

def no_symbol(s):
    return all(c.isalnum() for c in s)

def char_rep(s):
    return any(s[i]==s[i+1]==s[i+2]==s[i+3] for i in range(len(s)-3))

def number_sequence(s):
    t = '01234567890'
    for i in range(len(s)-3):
        if s[i:i+4] in t or s[i:i+4][::-1] in t:
            return True
    return False


def letter_sequence(s):
    t = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    for i in range(len(s)-3):
        if s[i:i+4] in t or s[i:i+4][::-1] in t:
            return True
    return False

def keyboard_pattern(s):
    row1 = "!@#$%^&*()_+"
    row2 = "qwertyuiop"
    row3 = "asdfghjkl"
    row4 = "zxcvbnm"
    s = s.replace('-', '_').replace('=', '+')
    # change string
    s = s.lower()
    for i in range(len(s)-3):
        if s[i:i+4] in row1 or s[i:i+4][::-1]in row1:
            return True
        if s[i:i+4] in row2 or s[i:i+4][::-1] in row2:
            return True
        if s[i:i+4] in row3 or s[i:i+4][::-1] in row3:
            return True
        if s[i:i+4] in row4 or s[i:i+4][::-1] in row4:
            return True
    return False

s = input()
c=0

if less_than_8_char(s):
    c += 1
    print("Less than 8 characters")

if no_lower_case(s):
    print("No lowercase letters")
    c+=1

if no_upper_case(s):
    print("No uppercase letters")
    c+=1

if no_num(s):
    print("No numbers")
    c+=1

if no_symbol(s):
    print("No symbols")
    c+=1

if char_rep(s):
    print("Character repetition")
    c+=1

if number_sequence(s):
    print("Number sequence")
    c+=1

if letter_sequence(s):
    print("Letter sequence")
    c+=1

if keyboard_pattern(s):
    print("Keyboard pattern")
    c+=1

if c==0:
    print("OK")
