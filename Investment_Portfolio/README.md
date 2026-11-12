# Investment Portfolio Tracker

## Project Description

The Investment Portfolio Tracker is a Python-based application that helps users manage and track their stock investments.

Users can enter stock ticker symbols, buying prices, share quantities, and current market prices. The program calculates the total investment, current portfolio value, profit or loss, and profit/loss percentage.

The transaction summary is automatically saved into a CSV file for future reference.

## Features

- Enter stock ticker symbols.
- Validate stock symbols using a stock dataset.
- Enter buying price and number of shares.
- Enter current market price manually.
- Calculate total investment for each stock.
- Calculate current stock value.
- Calculate profit or loss.
- Calculate profit/loss percentage.
- Calculate total portfolio investment and value.
- Export portfolio summary into a CSV file.

## Technologies Used

- **Python 3** – Programming language.
- **CSV Module** – Reading and writing CSV files.
- **Dictionary** – Storing stock portfolio details.
- **File Handling** – Saving portfolio reports.

## Project Structure

```text
Investment_Portfolio/
│
├── portfolio.py
│
├── constituents.csv
│
├── portfolio_summary.csv
│
└── README.md
```

## Requirements

- Python 3.x
- Visual Studio Code (recommended)
- Stock dataset (`constituents.csv`)

No external Python packages are required.

## Dataset

The project uses an S&P 500 companies dataset to validate stock ticker symbols.

Dataset source:

https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv

## How to Run

**Step 1:** Download or clone the project.

**Step 2:** Open the project folder in Visual Studio Code.

**Step 3:** Make sure `portfolio.py` and `constituents.csv` are in the same folder.

**Step 4:** Open the VS Code terminal.

**Step 5:** Run the program:

```bash
python portfolio.py
```

**Step 6:** Enter the requested details:

- Stock ticker symbol
- Buying price
- Number of shares
- Current market price

The program calculates the portfolio summary automatically.

## Sample Input

```text
Enter stock ticker symbol: AAPL
Enter buying price: 150
Enter number of shares: 10
Enter current market price: 180
```

## Sample Output

```text
===== INVESTMENT PORTFOLIO TRACKER =====

Stock added successfully!

========== PORTFOLIO SUMMARY ==========

Stock: AAPL
Total Investment: ₹ 1500.0
Current Value: ₹ 1800.0
Profit/Loss: ₹ 300.0
Profit/Loss Percentage: 20.0 %

========== TOTAL PORTFOLIO ==========

Total Investment: ₹ 1500.0
Total Current Value: ₹ 1800.0
Total Profit/Loss: ₹ 300.0

Portfolio summary saved successfully!
File created: portfolio_summary.csv
```

## Calculation Methods

**Total Investment**

Total Investment = Buying Price × Number of Shares

**Current Value**

Current Value = Current Market Price × Number of Shares

**Profit or Loss**

Profit/Loss = Current Value − Total Investment

**Profit/Loss Percentage**

Profit/Loss Percentage = (Profit/Loss ÷ Total Investment) × 100

## Output File

The program automatically generates `portfolio_summary.csv`, which stores the calculated stock investment details and portfolio summary.

## Learning Outcomes

Through this project, I learned:

- Python dictionaries and data structures.
- Reading and writing CSV files.
- File handling in Python.
- Input validation.
- Mathematical calculations using Python.
- Working with stock datasets.
- Generating automated reports.

## Limitations

- Current stock prices are entered manually.
- The project currently processes one stock per execution.
- It does not connect to a live stock market API.

## Author

Python Beginner Project

## License

This project is developed for educational and learning purposes. It is not intended to provide financial or investment advice.