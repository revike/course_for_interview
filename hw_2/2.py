class ItemDiscount:
    def __init__(self):
        self.__name = 'iPhone'
        self.__price = 1500


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Product - {self.__name}; price - {self.__price}$'


subsidiary = ItemDiscountReport()
print(subsidiary.get_parent_data())
