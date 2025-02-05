import sys

def capital_city(capital):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    if capital in capital_cities.values():
        for val in capital_cities:
            if capital_cities[val] == capital:
                for key, value in states.items():
                    if val == value:
                        print(key)
    else:
        print("Unknown capital city")

if len(sys.argv) > 2 or len(sys.argv) < 2:
    exit()

if __name__ == '__main__':
    capital_city(sys.argv[1])