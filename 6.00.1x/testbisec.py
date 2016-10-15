# Paste your code into this box
def bisection():
    balance = 320000
    aI = 0.2
    month = 12
    while month != 0:
        monthrate = aI / 12
        lower = balance / 12
        I = (aI /(12.0)) * balance
        upper = (balance * (1 + monthrate ) ** 12)/12.0
        balance += I
        ded = (lower + upper)/2
        balance -= ded
        month -= 1
    print balance
