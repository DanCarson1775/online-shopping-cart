class ShoppingCart:
    """
    Represents a customer's shopping cart.
    """
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []


    def add_item(self, item_to_purchase):
        """
        Adds an item to the cart_items list.
        """
        self.cart_items.append(item_to_purchase)


    def remove_item(self, item_name):
        """
        Removes an item from the cart. If not found, outputs nothing removed.
        """
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")


    def modify_item(self, item_to_purchase):
        """
        Modifies an item from the cart.
        """
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                item_found = True
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0.0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                break

        if not item_found:
            print("Item not found in cart. Nothing modified.")
    

    def get_num_items_in_cart(self):
        """
        Returns quantity of all items in cart.
        """
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity


    def get_cost_of_cart(self):
        """
        Determines and returns the total cost of items in the cart.
        """
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost


    def print_total(self):
        """
        Outputs total of objects in the cart or if the cart is empty.
        """
        print("\nOUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}\n")

        if not self.cart_items:
            print("SHOPPING CART IS EMPTY\n")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart():.2f}")


    def print_descriptions(self):
        """
        Outputs each items description.
        """
        print("\nOUTPUT ITEMS' DESCRIPTION")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY\n")
        else:
            for item in self.cart_items:
                item.print_item_description()
            print()
