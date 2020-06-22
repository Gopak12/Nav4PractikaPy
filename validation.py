DAYS_OF_THE_WEEK = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

class Validation:
    def check_name(s):
        return str.isalpha(s)

    def check_price(a):
        if not (a > 0):
            return False
        return True

    def check_departure_day(s):
        return s.lower() in DAYS_OF_THE_WEEK
