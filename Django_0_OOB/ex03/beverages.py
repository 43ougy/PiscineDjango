class HotBeverage:
    def __init__(self, name="hot beverage", price=0.30):
        self.name = name
        self.price = price
    def __str__(self):
        return f"""
    name : {self.name}
    price : {self.price:.2f}
    description : {self.description()}"""
    def description(self):
        return "Just some hot water in a cup."

class Coffee(HotBeverage):
    def __init__(self, name="coffee", price=0.40):
        super().__init__(name, price)
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self, name="tea"):
        super().__init__(name)

class Chocolate(HotBeverage):
    def __init__(self, name="cappuccino", price=0.50):
        super().__init__(name, price)
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self, name="coffee", price=0.45):
        super().__init__(name, price)
    def description(self):
        return "Un po’ di Italia nella sua tazza!"

def hot_beverage():
    hb = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    choco = Chocolate()
    cappu = Cappuccino()

    print(f"""
    {hb}
    {coffee}
    {tea}
    {choco}
    {cappu}
    """)


if __name__ == '__main__':
    try:
        hot_beverage()
    except Exception as e:
        print(e)