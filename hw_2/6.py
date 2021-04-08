class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Product - {self.name}; price - {self.price}$'


class ItemDiscountReportName(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        disc = self.price * 50 / 100
        return f'Product - {self.name}; price - {disc}$'

    def get_parent_data(self):
        return f'Product - {self.name}; price - {self.price}$'

    def get_info(self):
        return self.name


class ItemDiscountReportPrice(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        disc = self.price * 50 / 100
        return f'Product - {self.name}; price - {disc}$'

    def get_parent_data(self):
        return f'Product - {self.name}; price - {self.price}$'

    def get_info(self):
        return self.price


subsidiary_name = ItemDiscountReportName('iPhone', 1500, 50)
print(subsidiary_name.get_info())

subsidiary_price = ItemDiscountReportPrice('iPhone', 1500, 50)
print(subsidiary_price.get_info())
