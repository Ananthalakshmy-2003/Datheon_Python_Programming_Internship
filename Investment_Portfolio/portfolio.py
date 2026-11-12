
import csv
import os

portfolio = {}


# Step 1: Load stock symbols
def load_stocks():

    filename = "constituents.csv"

    if not os.path.exists(filename):
        print("Stock dataset not found!")
        return []

    stocks = []

    with open(filename, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            symbol = row["Symbol"].strip().upper()
            stocks.append(symbol)

    return stocks


# Step 2: Add stock details
def add_stock(stocks):

    symbol = input("\nEnter stock ticker symbol: ").upper().strip()

    if symbol not in stocks:
        print("Invalid stock symbol!")
        return

    if symbol in portfolio:
        print("This stock is already added!")
        return

    try:
        buy_price = float(input("Enter buying price: "))
        quantity = int(input("Enter number of shares: "))
        current_price = float(input("Enter current market price: "))

        if buy_price <= 0 or quantity <= 0 or current_price <= 0:
            print("Values must be greater than zero!")
            return

    except ValueError:
        print("Please enter valid numeric values!")
        return

    portfolio[symbol] = {
        "buy_price": buy_price,
        "quantity": quantity,
        "current_price": current_price
    }

    print("Stock added successfully!")


# Step 3: Calculate portfolio
def calculate_portfolio():

    total_investment = 0
    total_current_value = 0

    print("\n========== PORTFOLIO SUMMARY ==========")

    for symbol, details in portfolio.items():

        buy_price = details["buy_price"]
        quantity = details["quantity"]
        current_price = details["current_price"]

        investment = buy_price * quantity
        current_value = current_price * quantity

        profit_loss = current_value - investment
        percentage = (profit_loss / investment) * 100

        total_investment += investment
        total_current_value += current_value

        print("\nStock:", symbol)
        print("Total Investment: ₹", round(investment, 2))
        print("Current Value: ₹", round(current_value, 2))
        print("Profit/Loss: ₹", round(profit_loss, 2))
        print("Profit/Loss Percentage:", round(percentage, 2), "%")

    total_profit_loss = total_current_value - total_investment

    print("\n========== TOTAL PORTFOLIO ==========")
    print("Total Investment: ₹", round(total_investment, 2))
    print("Total Current Value: ₹", round(total_current_value, 2))
    print("Total Profit/Loss: ₹", round(total_profit_loss, 2))


# Step 4: Save portfolio to CSV
def save_portfolio():

    filename = "portfolio_summary.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Stock Symbol",
            "Buy Price",
            "Quantity",
            "Current Price",
            "Total Investment",
            "Current Value",
            "Profit/Loss",
            "Profit/Loss Percentage"
        ])

        for symbol, details in portfolio.items():

            buy_price = details["buy_price"]
            quantity = details["quantity"]
            current_price = details["current_price"]

            investment = buy_price * quantity
            current_value = current_price * quantity
            profit_loss = current_value - investment
            percentage = (profit_loss / investment) * 100

            writer.writerow([
                symbol,
                buy_price,
                quantity,
                current_price,
                investment,
                current_value,
                profit_loss,
                round(percentage, 2)
            ])

    print("\nPortfolio summary saved successfully!")
    print("File created:", filename)


# Step 5: Main program
def main():

    stocks = load_stocks()

    if not stocks:
        return

    print("\n===== INVESTMENT PORTFOLIO TRACKER =====")

    add_stock(stocks)

    if portfolio:
        calculate_portfolio()
        save_portfolio()


if __name__ == "__main__":
    main()
