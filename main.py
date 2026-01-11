"""
Module 4 - Portfolio Milestone

Step 1: Build the ItemToPurchase class.
Step 2: In main.py, prompt user for item data for two items (name, price, quantity).
Step 3: Add costs of both items and output their totals and the toal cost of both items.

User will be prompted to enter name, price, and quantity data for two items.
The total cost of each item is calculated seperatly and output to the user, followed but the total cost of both items.
"""


class ItemToPurchase:
    """Represents item to be purchased based on item attributes and cost."""

    def __init__(self):
        """Default Constructor."""
        self.item_name = "none"
        self.item_price = 0.0
        self. item_quantity = 0

    def print_item_cost(self):
        """Calculates cost of item and prints to output."""
        cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${cost}")


"""Main - Entry Point"""
if __name__ == "__main__":
    
    print("Welcome to the Online Shopping Calculator!\n")

    # Create two objects using the ItemToPurchase class
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    # Prompt user for two items
    print("Item 1")
    item1.item_name = input("Enter the item name: ")
    item1.item_price = float(input("Enter the item price: "))
    item1.item_quantity = int(input("Enter the item quantity: "))

    print("\nItem 2")
    item2.item_name = input("Enter the item name: ")
    item2.item_price = float(input("Enter the item price: "))
    item2.item_quantity = int(input("Enter the item quantity: "))

    # Calculate total cost and print out to user
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"\nTotal: ${total_cost}")
