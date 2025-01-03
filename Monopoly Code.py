class space:
    def __init__(self, name, type, number):
        self.name = name
        self.type = type
        self.number = number
class property(space):
    def __init__(self, colour, rent, rent1, rent2, rent3, rent4, rent_hotel, house_cost, hotel_cost, price):
        self.colour = colour
        self.rent = rent
        self.rent1 = rent1
        self.rent2 = rent2
        self.rent3 = rent3
        self.rent4 = rent4
        self.rent_hotel = rent_hotel
        self.house_cost = house_cost
        self.hotel_cost = hotel_cost
        self.price = price
class station(space):
    def __init__(self, price, rent):
        self.price = price
        self.rent = rent
class utility(space):
    def __init__(self, price):
        self.price = price


