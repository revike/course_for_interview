class ItemDiscount:
    def __init__(self):
        self.name = 'iPhone'
        self.price = 1500


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Product - {self.name}; price - {self.price}$'


subsidiary = ItemDiscountReport()
print(subsidiary.get_parent_data())
