from __future__ import annotations
import sys

SORTING = {
    '1' : 'name',
    '2' : '-name',
    '3' : 'destination',
    '4' : '-destination',
    '5' : 'flight_number',
    '6' : '-flight_number',
    '7' : 'price',
    '8' : '-price'
}

class Program:
    def __init__(self, collection):
        self.collection = collection

    def menu(self, file):
        t = int(input("enter your choice: "))
        if not (0 <= t <= 15):
            raise Exception("invalid type " + str(t))
        if t == 0:
            sys.exit(0)
        elif 1 <= t <= 8:
            self.collection.sort_by(SORTING[str(t)])
            file.make_change(self.collection.aeroflots)
        elif t == 9:
            destination = input("Enter destination: ")
            print(*self.collection.get_by_value(destination), sep="\n")
        elif t == 10:
            name = input("Enter name: ")
            print(*self.collection.get_by_value(name), sep="\n")
        elif t == 11:
            departure_day = input("Enter departure day: ")
            print(*self.collection.get_by_value(departure_day), sep="\n")
        elif t == 12:
            s = input("enter new aeroflot in format : 'name' 'destination' 'flight number' 'departure day' 'price' without quotes:\n")
            self.collection.add_aeroflot(s)
            file.make_change(self.collection.aeroflots)
        elif t == 13:
            index = int(input("enter index: "))
            self.collection.del_aeroflot(index)
            file.make_change(self.collection.aeroflots)
        elif t == 14:
            index, field, new_value = input("enter index, field, new_value: ").split()
            index = int(index)
            self.collection.edit_aeroflot(index, field, new_value)
            file.make_change(self.collection.aeroflots)
        elif t == 15:
            print(*self.collection.aeroflots)



