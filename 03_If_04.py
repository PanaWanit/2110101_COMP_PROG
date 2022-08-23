def valid(n):
    if len(n) != 10:
        return False
    if n[0] != "0" or n[1] in "0123457":
        return False
    return True
print("Mobile number" if valid(input())==True else "Not a mobile number")
