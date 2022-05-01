moneyOwed = float(input('What is the mortgate amount? '))
mortgageRate = float(input('What is the mortgage rate? '))
monthlyRate = mortgageRate/100/12
mortgagePayment = float(input('What is your mortgage payment? '))
monthsToCalculation = int(input('After how many months would you like to see remaining balance for? '))
months = 0
totalInterestPaid = 0
while (True):
    if moneyOwed > 0:
        interestPaid = moneyOwed * monthlyRate
        # reduce moneyOwed
        moneyOwed = moneyOwed - mortgagePayment
        #add interest
        moneyOwed = moneyOwed + interestPaid
        months = months + 1
        totalInterestPaid = totalInterestPaid + interestPaid
        print('The remaining balance after', months, ' months is', moneyOwed, ' Interest paid for the month is ', interestPaid)

    else:
        break

print('It took ', months, ' to pay off the loan with total interest of ', totalInterestPaid)
