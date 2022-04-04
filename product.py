class Product(object):

    products = {"Colombian Roast": 8.45, "Pumpkin Spice": 10.35, "Jedi Java": 13.25, "Tastea": 6.75, "Earl Grey": 4.50, "Westminster": 1.95}

    def __init__(self, product, productPrice):
        if product in Product.products:
            self.product = product
            self.productPrice = productPrice
        else:
            raise TypeError('Invalid product type.')

    def __str__(self):
        return f'{self.product}, {self.productPrice}'

    def get_product(self):
        return self.product