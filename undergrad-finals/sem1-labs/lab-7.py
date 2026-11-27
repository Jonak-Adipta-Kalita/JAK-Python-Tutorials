# Q1 - Electricity Bill
def calculateBill(unitsConsumed, ratePerUnit, taxPercent=5.0):
    base = unitsConsumed * ratePerUnit
    tax = base * taxPercent / 100
    total = base + tax

    print(f"Base Amount: {base:.2f}")
    print(f"Tax Amount: {tax:.2f}")
    print(f"Total Amount: {total:.2f}")


units = int(input())
rate = float(input())
custom_tax = float(input())

if custom_tax == -1:
    calculateBill(units, rate)
else:
    calculateBill(units, rate, custom_tax)


# Q2 - Bank Ledger
def deposit(amount):
    global totalBalance
    localMessage = "Deposit Successful"
    totalBalance += amount
    print(localMessage)


def withdraw(amount):
    global totalBalance
    if amount <= totalBalance:
        totalBalance -= amount
        print("Withdrawal Successful")
    else:
        insufficientFlag = True
        print("Insufficient Balance")


totalBalance = float(input())
depositAmount = float(input())
withdrawAmount = float(input())

deposit(depositAmount)
withdraw(withdrawAmount)

print(f"Final Balance: {totalBalance:.2f}")
