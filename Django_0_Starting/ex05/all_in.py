import sys

def capital_city(args):
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

    val = args.split(",")
    for ciorca in val:
        ret = ciorca.strip()
        if ret in states.keys():
            for keys in states:
                if keys.upper() == ret.upper():
                    print(keys, "is a states")
        elif ret in capital_cities.values():
            for val in capital_cities:
                if capital_cities[val].upper() == ret.upper():
                    for keys in states:
                        if states[keys] == val:
                            print(capital_cities[val], "is the capital of", keys)
        else:
            print(ret, "is neither a city or a capital")
        

if len(sys.argv) > 2 or len(sys.argv) < 2:
    exit()

if __name__ == '__main__':
    capital_city(sys.argv[1])