word=input();sen=input()
print(''.join([x if x not in ",\'\"()." else " " for x in sen]).split().count(word))
