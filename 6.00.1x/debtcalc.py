# Paste your code into this box
import time
def debtcalc():
    start = time.time()
    balance = 320000
    annualInterestRate = 0.2
    mI = annualInterestRate/12
    #num = 1      
    balance1 = balance    
    total = 0
    totint = 0
    tot = 0
    upper = (balance * (1 + mI)** 12) / 12.0
    lower = balance / 12
    
    while balance >= 0:
        balance = balance1
        
        minmpay = (lower + upper)/2
        #print 'minmpay now is: ' + str(minmpay) 
        #minmpay = num * 0.01
        for i in range (0,12):
            #print i
            balance = round(balance - minmpay,2)
            #print 'current balance is : ' + str(balance)
            interest = round((balance * annualInterestRate/12),2)
            balance += interest
            totint += interest
            #print 'month ' + str(i) + 'balance is : ' + str(balance)
        if i != 11:
            if balance <= 0:
                upper = minmpay
                balance = balance1
            else:
                lower = minmpay
                balance = balance1    
        else:
            if round(balance,1) == 0:
                break
            elif balance <= 0:
                upper = minmpay
                balance = balance1
            else:
                lower = minmpay
                balance = balance1
        #num += 1
    #print round(balance,1) 
    if round(balance,1) == 0:
        print 'Lowest payment: ' + str(round(minmpay,2))
    #else:
    #    print 'Lowest payment: ' + str(minmpay)
    #stop = time.time()
    #print stop - start
