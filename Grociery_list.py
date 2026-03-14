"""2)	Write a program that:
•	Has a predefined dictionary of groceries with prices.
•	Lets the user "add" items by typing their names.
•	For each valid item, asks for the quantity.
•	Keeps adding to the cart until the user types "checkout".
•	Displays a final bill: each item, quantity, subtotal, and total."""


def main():
    inv = {"apple": 0.5, "milk": 3.0, "bread": 2.5, "egg": 4.0, "banana": 0.3, "cheese": 5.0}
    cart = {}
    print("Welcome")
    print(f"Available: {', '.join(inv.keys())}\nType 'checkout' to finish.")

    while (item := input("\nItem: ").lower()) != 'checkout':
        if item in inv:
            try:
                qty = int(input(f"How many {item}s? "))
                if qty > 0:
                    cart[item] = cart.get(item, 0) + qty
                else:
                    print("Enter a positive number.")
            except ValueError:
                print("Invalid input.")
        else:
            print("Not in stock.")

    print(f"\n{'ITEM':<10} | {'QTY':<3} | TOTAL\n" + "-"*25)
    total = sum(inv[i] * q for i, q in cart.items())
    for i, q in cart.items():
        print(f"{i.title():<10} | {q:<3} | ${inv[i]*q:.2f}")
    print("-" * 25 + f"\nTotal: ${total:.2f}")

if __name__ == "__main__":
    main()