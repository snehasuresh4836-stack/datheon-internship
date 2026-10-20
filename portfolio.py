import csv
import yfinance as yf


def load_symbols():
    symbols = set()

    with open("sp500_tickers.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            symbols.add(row["Symbol"].strip().upper())

    return symbols


def get_current_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")

    if data.empty:
        return None

    return float(data["Close"].iloc[-1])


def calculate_performance(buy_price, shares, current_price):
    invested_amount = buy_price * shares
    current_value = current_price * shares
    gain_loss = current_value - invested_amount

    if invested_amount != 0:
        gain_loss_percentage = (gain_loss / invested_amount) * 100
    else:
        gain_loss_percentage = 0

    return invested_amount, current_value, gain_loss, gain_loss_percentage

def save_summary(symbol, buy_price, shares, current_price,
                 invested_amount, current_value, gain_loss,
                 gain_loss_percentage):

    file_exists = False

    try:
        with open("portfolio_summary.csv", "r", encoding="utf-8"):
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open("portfolio_summary.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Stock Symbol",
                "Buy Price",
                "Shares",
                "Current Price",
                "Total Invested",
                "Current Value",
                "Gain/Loss",
                "Gain/Loss %"
            ])

        writer.writerow([
            symbol,
            f"{buy_price:.2f}",
            shares,
            f"{current_price:.2f}",
            f"{invested_amount:.2f}",
            f"{current_value:.2f}",
            f"{gain_loss:.2f}",
            f"{gain_loss_percentage:.2f}"
        ])

def main():
    symbols = load_symbols()

    print("\n========================================")
    print("     STOCK PORTFOLIO TRACKER")
    print("========================================")
    

    symbol = input("Enter S&P 500 stock symbol: ").strip().upper()

    if symbol not in symbols:
        print("Invalid symbol. Please enter a valid S&P 500 ticker.")
        return

    try:
        buy_price = float(input("Enter your buy price: "))
        shares = int(input("Enter number of shares: "))

        if buy_price <= 0 or shares <= 0:
            print("Buy price and number of shares must be greater than zero.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    print("\nFetching current stock price...")

    current_price = get_current_price(symbol)

    if current_price is None:
        print("Unable to retrieve the current stock price.")
        return

    invested_amount, current_value, gain_loss, gain_loss_percentage = calculate_performance(
        buy_price,
        shares,
        current_price
    )

    print("\n----------- PORTFOLIO SUMMARY -----------")
    print(f"Stock Symbol       : {symbol}")
    print(f"Buy Price          : ${buy_price:.2f}")
    print(f"Number of Shares   : {shares}")
    print(f"Current Price      : ${current_price:.2f}")
    print(f"Total Invested     : ${invested_amount:.2f}")
    print(f"Current Value      : ${current_value:.2f}")
    print(f"Gain/Loss          : ${gain_loss:.2f}")
    print(f"Gain/Loss %        : {gain_loss_percentage:.2f}%")
    print("-----------------------------------------")
    save_summary(
    symbol,
    buy_price,
    shares,
    current_price,
    invested_amount,
    current_value,
    gain_loss,
    gain_loss_percentage
)

print("\nPortfolio summary saved to portfolio_summary.csv")

if __name__ == "__main__":
    main()