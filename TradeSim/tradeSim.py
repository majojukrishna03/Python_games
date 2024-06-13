

import random

cash = 0
holdings = {}
available_stocks = [{"name": "Apple", "price": 150},
                    {"name": "Google", "price": 2500},
                    {"name": "Microsoft", "price": 300}]

def portfolio(cash):
    if cash == 0 and holdings:
        print("Current portfolio is as follows : ")
        print(f"  Available Virtual amount is {cash}")
        print("Current Stock Holdings are as follow : ")
        for stock, quantity in holdings.items():
            print(f"  {stock} : {quantity} shares")
        print()
        print("-------------------------------------------------------")
    elif cash == 0 and not holdings:
        print("You have no portfolio!!")
        print("-------------------------------------------------------")
    else:
        print("Current portfolio is as follows : ")
        print(f"  Available Virtual amount is {cash}")
        print("Current Stock Holdings are as follow : ")
        for stock, quantity in holdings.items():
            print(f"  {stock} : {quantity} shares")
        print()
        print("-------------------------------------------------------")

def setVirtualamount(cash):
    while True:
        amount = int(input("Enter the virtual amount to be added: "))
        if amount == 0:
            print("Amount cannot be 0. Please try again")
            print("-------------------------------------------------------")
            continue
        elif amount < 0:
            print("Amount cannot be negative. Please try again!!")
            print("-------------------------------------------------------")
            continue
        else:
            cash += amount
            break
    return cash

def buyStock(cash, stock_purchase):
    stock_price = 0
    total_price = 0
    print("Initiating stock purchase...")
    for i in range(len(available_stocks)):
        print(f"{i}. {available_stocks[i]['name']} : {available_stocks[i]['price']}")
    stock_serial = (input("Enter the serial number of the stock for purchase : "))
    while True:
        quantity = int(input("Enter the number of shares for purchase : "))
        if quantity == 0:
            print("Quantity cannot be 0. Please try another value.")
            continue
        else:
            break

    stock_details = available_stocks[int(stock_serial)]
    stock_name = stock_details['name']
    stock_price += stock_details['price']
    total_price += stock_price * quantity

    if cash < total_price:
        return stock_purchase, total_price
    else:
        if stock_name not in holdings:
            holdings[stock_name] = quantity
        else:
            holdings[stock_name] += quantity
        stock_purchase = True
        return stock_purchase, total_price

def sellStock():
    global cash
    print("Initiating stock sale...")
    if not holdings:
        print("No stocks available to sell!")
        print("----------------------------------------------------")
        return False
    for i, stock in enumerate(holdings):
        print(f"{i}. {stock} : {holdings[stock]} shares")
    stock_serial = int(input("Enter the serial number of the stock to sell: "))
    stock_name = list(holdings.keys())[stock_serial]
    stock_quantity = holdings[stock_name]
    while True:
        quantity = int(input("Enter the number of shares to sell: "))
        if quantity == 0:
            print("Quantity cannot be 0. Please try another value.")
            continue
        elif quantity > stock_quantity:
            print("Not enough shares to sell. Please try another value.")
            continue
        else:
            break
    stock_price = next(item['price'] for item in available_stocks if item["name"] == stock_name)
    total_sale = stock_price * quantity
    holdings[stock_name] -= quantity
    if holdings[stock_name] == 0:
        del holdings[stock_name]
    cash += total_sale
    return True

def updateStockPrices():
    for stock in available_stocks:
        change_percent = random.uniform(-0.05, 0.05)  # Simulate a daily price change within +/- 5%
        stock['price'] += stock['price'] * change_percent
        stock['price'] = round(stock['price'], 2)  # Round to 2 decimal places
    print("Stock prices have been updated for the new day.")
    print("----------------------------------------------------")

def main():
    global cash
    days = 0
    max_days = int(input("Enter the number of days to run the simulation: "))
    simulation = True
    while days < max_days:
        updateStockPrices()  # Update stock prices at the start of each day
        print(f"Day {days + 1}")
        while True:    
            print()
            print("Welcome to the Stock Trading Simulator!!")
            print()
            print("1. Set virtual amount for trading")
            print("2. Buy a stock")
            print("3. Sell a stock")
            print("4. View current holdings")
            print("5. End the day")
            print("6. Exit")
            print("----------------------------------------------------")
            a = input("Enter the serial number of the operation listed: ")
            if a == '1':
                cash = setVirtualamount(cash)
                print("Available Virtual amount is: ", cash)
                print("----------------------------------------------------")
                continue
            elif a == '2':
                stock_purchase = False
                purchase, stock_total = buyStock(cash, stock_purchase)
                if purchase == False:
                    print("Available virtual amount is less than stock price. Please add enough amount and try again.")
                    print("Stock purchase failed!!")
                    print("----------------------------------------------------")
                    continue
                else:
                    cash -= stock_total
                    print("Stock Purchase Successful.")
                    print("Available Virtual amount is: ", cash)
                    print("----------------------------------------------------")
                    continue
            elif a == '3':
                success = sellStock()
                if success:
                    print("Stock sale successful")
                    print("Available Virtual amount is: ", cash)
                    print("----------------------------------------------------")
                continue
            elif a == '4':
                portfolio(cash)
                continue
            elif a == '5':
                print("Ending the day...")
                print("----------------------------------------------------")
                break
            elif a == '6':
                simulation = False
                break
            else:
                print("Please enter the serial number of the operation listed!!")
                print("----------------------------------------------------")
                continue
        if simulation == False:
            print("Exiting the simulation....")
            break
        days += 1
    print("Simulation has ended. Thank you for using the stock trading simulator. Goodbye!!")

main()
