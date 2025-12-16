def main():
    print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"

   Prosperity comes in threes!
========================================

ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
Flying Carpet................$119.99
Phoenix Feather...............$14.99
Time Turner..............$84.99
Enchanted Sword.............$65.99
Potion of Luck...............$11.99
Crystal Ball................$39.99
""")

    # Shopkeeper's rule: All purchases must be at least 3 items for good luck!
    # (Don't worry - the shopkeeper checks every order himself)
    item = input("Item Name:")
    price = float(input("Price of Item:"))
    quantity = int(input("Quantity of Item:"))

    # TODO: Calculate subtotal, tax, and total
    subtotal = price*quantity
    # Tax rate: 9.5%
    tax=subtotal*0.095
    total=subtotal+tax

    # TODO: Round total to 2 decimal places using round()
    subtotal = round(subtotal, 2)
    tax = round(tax, 2)
    total = round(total, 2)

    # TODO: Print receipt
    print("--------------------------")

    print(f"{item} x{quantity} @${price} each")

    print("--------------------------")
    # Print subtotal, tax, and total here
    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total}")


    print("\nThank you for shopping at\nthe Peculiar Emporium!")

    # The Peculiar Emporium


if __name__ == "__main__":
    main()
