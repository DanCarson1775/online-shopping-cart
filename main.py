"""
Module 6 - Portfolio Milestone

Step 4: Building the Shopping Cart class.
Step 5: Creating and implementing the menu function.
Step 6: Create and implement the output to the shopping cart menu including item descriptions.

Step 1: Build the ItemToPurchase class.
Step 2: In main.py, prompt user for item data for two items (name, price, quantity).
Step 3: Add costs of both items and output their totals and the toal cost of both items.

Online shopping cart application. User is able to add, remove, change quantity, and output totals from items.
Application consists of
    main.py
    shopping_cart.py
    item_to_pruchase.py
"""


# Imports
from item_to_purchase import ItemToPurchase
from shopping_cart import ShoppingCart


def print_menu(cart):
    """
    Outputs the menu options for shopping cart and user input. Then calls the corresponding functions.
    """
    menu = (
        "MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit"
    )

    # Get user menu choice
    while True:
        print(menu)
        choice = input("Choose an option: ").lower().strip()

        # Quits out of application
        if choice == "q":
            break
        
        # Get new item data and add too the cart
        elif choice == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            # Create item object with data
            new_item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(new_item)
            print()

        # Removes an item from the cart
        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
            print()

        # Change the quantity of an item in the cart
        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name: ")
            quantity = input("Enter the new quantity: ")
            # Dummy value creation
            modified_item = ItemToPurchase(name, item_quantity=quantity)
            cart.modify_item(modified_item)
            print()

        # Shows the item name and its description    
        elif choice == "i":
            cart.print_descriptions()

        # Totals and outputs cart item values
        elif choice == "o":
            cart.print_total()

        # Catch bad input from user
        else:
            print("Invalid option. Please try again.")


def main():
    """
    Main function. Create shopping cart and run menu.
    """
    # Get user header data
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print()

    my_cart = ShoppingCart(customer_name, current_date)
    print_menu(my_cart)


# Program entry point
if __name__ == "__main__":
    main()
    


    """
    Milestone 1 Commented out to run project.
    """
    # print("Welcome to the Online Shopping Calculator!\n")

    # # Create two objects using the ItemToPurchase class
    # item1 = ItemToPurchase()
    # item2 = ItemToPurchase()

    # # Prompt user for two items
    # print("Item 1")
    # item1.item_name = input("Enter the item name: ")
    # item1.item_price = float(input("Enter the item price: "))
    # item1.item_quantity = int(input("Enter the item quantity: "))

    # print("\nItem 2")
    # item2.item_name = input("Enter the item name: ")
    # item2.item_price = float(input("Enter the item price: "))
    # item2.item_quantity = int(input("Enter the item quantity: "))

    # # Calculate total cost and print out to user
    # print("\nTOTAL COST")
    # item1.print_item_cost()
    # item2.print_item_cost()

    # total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    # print(f"\nTotal: ${total_cost}")
