color_line = [x for x in open(input().strip(), "r").readlines()]
song_list = [x for x in open(input().strip(), "r").readlines()]

color = []

for i in color_line:
    for j in i.split():
        s = ""
        for c in j:
            if c.isalpha():
                s += c
        if s not in color:
            color.append(s.lower())

for word in song_list:
    j=0
    while j < len(word):
        ch=0
        for col in color:
            if word[j:j+len(col)].lower() != col:
                continue
            print("<" + col + ">" + word[j:j+len(col)] + "</>", end='')
            j += len(col)
            ch=1
            break
        if ch==1:
            continue
        if j!=len(word):
            print(word[j], end='')
        j+=1


