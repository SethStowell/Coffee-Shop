from address import Address

class Customer(object):

    def __init__(self, name, address):
        self.customers = []
        self.name = name
        newCustomer = Customer(name, address)
        self.customers.append(newCustomer)

    def __str__(self):
        return f'{self.name}, {self.address}'


