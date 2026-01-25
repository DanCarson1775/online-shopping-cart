class ItemToPurchase:
    """
    Represents item to be purchased based on item attributes and cost.
    """
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description


    def print_item_cost(self):
        """
        Prints calculated cost of item to output.
        """
        cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${cost}")


    def print_item_description(self):
        """
        Prints item name and description.
        """
        print(f"{self.item_name}: {self.item_description}")
