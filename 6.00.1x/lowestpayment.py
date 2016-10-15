import math
month = 12
mp = 0
p = 0
balance = float(raw_input("Enter balance after month 0 :"))
annualInterestRate = float(raw_input("enter annual interest rate: "))
#monthlyPaymentRate = float(raw_input("enter rate of minimum monthly payment: "))
for i in range (13,0,-1):
    print "month : " + str(13-i)
    paid = balance / i
    paid = round (paid, 2)
    mp = mp + paid
    print "Minimum monthly payment" + str(paid)
    balance = balance - paid
    balance = round(balance,2)
    #print "Remaining Balance" + str(balance)
    #print "unpaid balance after minimum payment" + str(balance)
    I = (annualInterestRate /(12.0)) * balance
    #print "interest charged" + str(I)
    balance = balance + I
    balance = round(balance,2)
    print "Remaining Balance : " + str(balance)
    
print "Total paid" + str(mp)
p = mp/12
#p = int(round(p*10.0)/10.0)
#x = p % 10
#if x >= 5:
#    p = p + (10-x)
#else:
 #   p = p - x

print "Lowest payment: " + str(p)

print "Finally after 12 months balance unpaid" + str(balance)



