from validation import Validation
from aeroflot import Aeroflot

def check_aeroflot(func):
    def wrapper(self, name, destination, flight_number, departure_day, price):
        if not Validation.check_name(name):
            raise Exception("invalid name " + name)
        if not Validation.check_name(destination):
            raise Exception("invalid destination " + destination)
        if not Validation.check_departure_day(departure_day):
            raise Exception("invalid departure_day " + departure_day)
        if not Validation.check_price(price):
            raise Exception("invalid price " + price)
        res = func(self, name, destination, flight_number, departure_day, price)
        return res
    return wrapper

def check_index(func):
    def wrapper(self, index):
        if not (0 <= index < len(self.aeroflots)):
            raise Exception("invalid index " + str(index) + f'\nenter index in range [0..{len(self.aeroflots)})')
        res = func(self, index)
        return res
    return wrapper

def check_edit(func):
    def wrapper(self, index, field, new_value):
        a = Aeroflot()
        field = field.lower()
        if not hasattr(a, field.lower()):
            raise Exception("Invalid field " + field)
        if not (0 <= index < len(self.aeroflots)):
            raise Exception("invalid index " + str(index) + f'\nenter index in range [0..{len(self.aeroflots)})')
        res = func(self, index, field, new_value)
        return res
    return wrapper
