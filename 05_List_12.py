name = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nick = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']
n = int(input())
for i in range(n):
    s = input()
    if s in name:
        print(nick[name.index(s)])
    elif s in nick:
        print(name[nick.index(s)])
    else:
        print('Not found')
