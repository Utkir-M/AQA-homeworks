class Address:
    index = '000000'
    city = 'unknown'
    street = 'unknown'
    house = '0'
    apart = '0'

    def __init__(self, index, city, street, house, apart):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apart = apart
