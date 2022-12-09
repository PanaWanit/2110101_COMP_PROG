
def knows(R, x, y):
    if x not in R:
        return False
    return y in R[x] 

def is_celeb(R, x):
    if x in R[x]:
        R[x].remove(x)
    if len(R[x])!=0:
        return False
    for person in R.keys():
        if person == x:
            continue
        if x not in R[person]:
            return False
    return True

def find_celeb(R):
    for person in R.keys():
        if is_celeb(R, person):
            return person
    return None
def read_relations():
    R = dict()
    while True:
        d = input().split()
        if len(d)==1:
            break

        if d[0] not in R:
            R[d[0]] = set()
        if d[1] not in R:
            R[d[1]] = set()

        if d[0] == d[1]:
            continue
        R[d[0]].add(d[1])
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c==None:
        print("Not Found")
    else:
        print(c)

exec(input().strip())
