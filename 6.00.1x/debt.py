def debt():
    balance = 3329
    aI = 0.2
    month = 1
    monthly = 0
    inte = 0
    while month != 13:
        mp = balance / 12
        balance -= mp
        interest = (balance * (aI/12))
        balance += interest
        monthly += mp
        inte += interest
        print 'Remaining balance: ' + str(balance)
        print monthly
        month += 1

    print balance
    print monthly/12
