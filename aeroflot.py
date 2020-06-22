class Aeroflot:
    def __init__(self, name='', destination='', flight_number='', departure_day='', price=''):
        self.name = name
        self.destination = destination
        self.flight_number = flight_number
        self.departure_day = departure_day
        self.price = price
    def __str__(self):
        out = self.name
        out += ' ' + self.destination
        out += ' ' + str(self.flight_number)
        out += ' ' + self.departure_day
        out += ' ' + str(self.price)
        return out
    def __contains__(self, item):
        return (
            item in self.name.lower() or
            item in self.destination.lower() or
            item == self.flight_number or
            item == self.departure_day.lower() or
            item == self.price
        )
