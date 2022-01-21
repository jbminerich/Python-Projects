def paybills():
    # ask user for income
    print('**Welcome to the billing program!!**')
    income = int(input('What is your income for this billing cycle?'))
    
    # loop through and keep asking user for bill name and amount until they enter STOP
    total = bills()
    # display total in bills and subtract from income
    net = income - total
    if net > 0:
        print(f"\nYour income of {income} and bill total of {total} results in a positive value of {net}")
    else:
        print(f"\nYour income of {income} and bill total of {total} results in a negative value of {net}")


def bills():
    active = True
    bill = {}
    print('\nBills function: when complete, type stop')
    
    while active:
        bill_add = input('Enter in the expense name and amount. Note: positive values only: (cheese 3)').split()
        if bill_add == ['stop']:
            values = bill.values()
            total = sum(values)
            active = False
            print(bill)
            return total
        else:
            bill[bill_add[0]] = int(bill_add[1])
 