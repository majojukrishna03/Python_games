def initializeWallet():
    wallet = {"balance": 0,"transaction_history": []}
    return wallet

def displayBalance(wallet):
    balance = wallet["balance"]
    print(f"Current balance: Rs.{balance}")

def addFunds(wallet, amount):
    if amount <= 0:
        print("Amount can't be negative or 0")
        return None

    wallet["balance"] += amount
    wallet["transaction_history"].append(f"Credit: +Rs.{amount}")

def makePayment(wallet, amount):
    if amount <= 0:
        print("Amount can't be negative or 0")
        return None
    if wallet["balance"] < amount:
        print("Insufficient funds!!!")
        return None

    wallet["balance"] -= amount
    wallet["transaction_history"].append(f"Debit: -Rs.{amount}")

def transactionHistory(wallet):
    print("Transaction History:")
    for transaction in wallet["transaction_history"]:
        print(transaction)


def useWallet():
    print("Welcome to wallet!!!")
    wallet=initializeWallet()

    while True:

        print("\n Menu:")
        print("a. View Balance:")
        print("b. Add Funds:")
        print("c. Make a paymnet")
        print("d. View Transaction History")
        print("e. Exit")

        choice=input("plese choose a option:").lower()

        if choice=="a":
            displayBalance(wallet)
            print("------------")
        if choice=="b":
            amount= float(input("Enter amount to add :Rs."))
            addFunds(wallet, amount)
            print("Amount added successfully.")
            print("------------")
        if choice=="c":
            amount=float(input("enter amount to pay :Rs."))
            makePayment(wallet, amount)
            print("Payment done successfully.")
            print("------------")
        if choice=="d":
            transactionHistory(wallet)
        if choice=="e":
            print("Thank you using the wallet.GoodBye!!")
            print("------------")
            break

useWallet()

