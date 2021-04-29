class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Product - {self.name}; price - {self.price}$'


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Product - {self.name}; price - {self.price}$'


parent = ItemDiscount('iPhone', 1500)
subsidiary = ItemDiscountReport('iPhone', 1500)

parent.name = 'Samsung'
parent.price = 1200

subsidiary.name = 'Samsung'
subsidiary.price = 1200

print(parent)
print(subsidiary.get_parent_data())
