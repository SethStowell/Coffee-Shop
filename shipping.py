from lineItem import LineItem

class Shipping(object):

    shippingMethods = {"Standard": 4.50 * weight + 1.86, "Express": 0 * weight + 4.65, "Bulk": 12.00 * weight + 0.95}

    def __init__(self, shippingMethod, shippingCost):
        if shippingMethod in Shipping.shippingMethods:
            self.shippingMethod = shippingMethod
            self.shippingCost = shippingCost
        else:
            raise TypeError('Invalid shipping method type.')

    def __str__(self):
        return f'{self.shippingMethod}{self.shippingCost}'

    def get_shippingMethod(self):
        return self.shippingMethod
