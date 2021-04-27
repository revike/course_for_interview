class ItemDiscount:
    def __init__(self):
        self._name = 'iPhone'
        self._price = 1500

    def __str__(self):
        return f'Product - {self._name}; price - {self._price}$'


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Product - {self._name}; price - {self._price}$'


parent = ItemDiscount()
print(parent)
