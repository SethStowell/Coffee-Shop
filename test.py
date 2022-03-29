from store import Store
from customer import Customer
from lineitem import LineItem
from order import Order
from product import Product
from shippingMethod import ShippingMethod
from address import Address

def test():
    print('\n----product test----')
    product = Product('Bubble Tea', 'tea', 13.50)
    print(Product)

    print('\n----shipping method test----')
    shippingMethod = ShippingMethod('FedEx, Faster and more expensive', 0.00, 4.65)
    print(shippingMethod)

    print('\n----address test----')
    address = Address('1100 North 56th Street', 'Lincoln', 'NE', '68504',)
    print(address)

    print('\n----line item test----')
    lineItem = LineItem(product, 3.5)
    print(lineItem)

    print('\n----order test 1----')
    order = Order(shippingMethod, address)
    print(order)

    print('\n----order test 2----')
    order.add(product, 3.5)
    order.add(product, 1)
    print(order)

    print('\n----customer test 1----')
    name = 'Lloyd Sommerer'
    customer = Customer(name, address)
    print(customer)

    print('\n----customer test 2----')

    customer.add(order)
    print(customer)

test()