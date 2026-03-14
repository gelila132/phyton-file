"""Build a program that:
•	Displays a list of snacks and drinks with item numbers and prices. 
•	Ask the user to choose items by number in a loop.
•	 Keeps track of selected items and their prices.
•	Ends when the user types "done".
•	Finally prints a receipt showing: List of selected items with prices and total cost """


menu = {
    "1": ("Coffee", 1.50),
    "2": ("Cake", 3.00),
    "3": ("Tea", 1.00),
    "4": ("Water", 1.00),
    "5": ("Bread", 2.00)
}

cart = []
print("Menu: " + ", ".join([f"{k}: {v[0]} (${v[1]})" for k, v in menu.items()]))

while True:
    choice = input("Enter item # (or 'done'): ").lower()
    if choice == 'done': break
    if choice in menu:
        cart.append(menu[choice])
        print(f"Added {menu[choice][0]}")
    else:
        print("Invalid choice.")

print("\n--- Receipt ---")
total = sum(item[1] for item in cart)
for name, price in cart:
    print(f"{name:10} ${price:.2f}")
print(f"Total:     ${total:.2f}")