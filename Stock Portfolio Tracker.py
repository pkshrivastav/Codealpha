class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, name, quantity, price):
        if symbol in self.stocks:
            print(f"Stock {symbol} already in portfolio. Updating quantity.")
            self.stocks[symbol]['quantity'] += quantity
            self.stocks[symbol]['price'] = price  # Update to the latest price
        else:
            self.stocks[symbol] = {'name': name, 'quantity': quantity, 'price': price}
        print(f"Added/Updated stock: {symbol} - {name} ({quantity} shares at ${price} each)")

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if quantity >= self.stocks[symbol]['quantity']:
                del self.stocks[symbol]
                print(f"Removed all shares of {symbol}.")
            else:
                self.stocks[symbol]['quantity'] -= quantity
                print(f"Removed {quantity} shares of {symbol}. Remaining: {self.stocks[symbol]['quantity']} shares.")
        else:
            print(f"Stock {symbol} not found in portfolio.")

    def view_portfolio(self):
        if not self.stocks:
            print("Portfolio is empty.")
            return
        total_value = 0
        print("Current Portfolio:")
        print(f"{'Symbol':<10} {'Name':<20} {'Quantity':<10} {'Price':<10} {'Total Value':<10}")
        print("-" * 60)
        for symbol, details in self.stocks.items():
            value = details['quantity'] * details['price']
            total_value += value
            print(f"{symbol:<10} {details['name']:<20} {details['quantity']:<10} ${details['price']:<10} ${value:<10}")
        print(f"\nTotal Portfolio Value: ${total_value}")

def main():
    portfolio = Portfolio()
    
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add/Update Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            name = input("Enter stock name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per share: "))
            portfolio.add_stock(symbol, name, quantity, price)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.view_portfolio()
        elif choice == '4':
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
