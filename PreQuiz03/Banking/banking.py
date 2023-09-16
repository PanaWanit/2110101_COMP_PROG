bank = dict()
owner = dict()


def add_money(name, account, value):
    owner[account] = name
    if name not in bank:
        bank[name] = dict()
    if account not in bank[name]:
        bank[name][account] = 0
    bank[name][account] += value

def ps(a):
    if float(int(a)) == a:
        return str(a)[:str(a).find('.')]
    return a

def deposit(name, account, amount):

    if (account in owner) and (owner[account]!=name): #already have owner for this account and this owner account doesn't match with this name
        print("Transaction Failed")
        return

    add_money(name, account, amount)
    print(name, '('+account+')', ps(bank[name][account]))

def withdraw(name, account, amount):
    if name not in bank:
        print("Transaction Failed")
        return
    if account not in bank[name]:
        print("Transaction Failed")
        return
    if bank[name][account] - amount < 0:
        print("Transaction Failed")
        return
    bank[name][account] -= amount
    print(name, '('+account+')', ps(bank[name][account]))

def transfer(name, account, amount, account_transferee):
    if name not in bank:
        print("Transaction Failed")
        return
    if account not in bank[name]:
        print("Transaction Failed")
        return
    if bank[name][account] - amount < 0:
        print("Transaction Failed")
        return

    if account_transferee not in owner: # no owner of this account
        print("Transaction Failed")
        return

    bank[name][account] -= amount
    bank[owner[account_transferee]][account_transferee] += amount
    print(name, '('+account+')', ps(bank[name][account]))
    print(owner[account_transferee], '('+account_transferee+')', ps(bank[owner[account_transferee]][account_transferee]))


for _ in range(int(input())):
    name, account, amount = input().split()
    add_money(name, account, float(amount))

inp = input().strip()
while inp != 'exit':
    name, account, opr = inp.split()[:3]
    if opr=='deposit':
        amount = float(inp.split()[3])
        deposit(name, account, amount)
    elif opr=='withdraw':
        amount = float(inp.split()[3])
        withdraw(name, account, amount)
    else: # transfer
        account_transferee, amount = inp.split()[3:]
        transfer(name, account, float(amount), account_transferee)
    inp = input().strip()
