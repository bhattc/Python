month = 12
mp = 0
balance = float(raw_input("Enter balance after month 0 :"))
annualInterestRate = float(raw_input("enter annual interest rate: "))
monthlyPaymentRate = float(raw_input("enter rate of minimum monthly payment: "))
for i in range (1,13):
    print "month : " + str(i)
    paid = balance * monthlyPaymentRate
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

print "Finally after 12 months balance unpaid" + str(balance)



