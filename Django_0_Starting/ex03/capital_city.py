import sys

def capital_city(city):
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

    if city in states.keys():
        for val in states:
            if val == city:
                print(capital_cities[states[val]])
    else:
        print("Unknown state")

if len(sys.argv) > 2 or len(sys.argv) < 2:
    exit()

if __name__ == '__main__':
    capital_city(sys.argv[1])