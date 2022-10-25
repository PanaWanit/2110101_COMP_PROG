all_set = [set([y for y in input().split()]) for x in range(int(input()))]
all_set += [set()]*(len(all_set)==0)
union = set.union(*all_set)
sec = set.intersection(*all_set)
print(len(union), len(sec), sep='\n')
