
def valid(s):
    if len(s) != 2:
        return False
    a = ["01", "02", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "51", "53", "55", "58"]
    return True if s in a else False

print("OK" if valid(input())==True else "Error")

