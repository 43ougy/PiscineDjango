import random
import beverages as bv

class CoffeeMachine:
    def __init__(self):
        self.TotalUsage = 10
        self.usage = 0
        self.breaks = False

    class EmptyCup(bv.HotBeverage):
        def __init__(self, name="empty cup", price=0.90):
            super().__init__(name, price)
        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            super().__init__(message)

    def repair(self):
        self.usage = 0
        self.breaks = False
        print("The coffee machine is now repaired")

    def serve(self, bever: bv.HotBeverage()):
        if self.breaks == True:
            raise self.BrokenMachineException()
        
        self.usage += 1

        if self.usage >= self.TotalUsage:
            self.breaks = True

        r = random.randint(1, 2)
        if r == 1:
            return self.EmptyCup()
        else:
            return bever
    

def machine():
    coffeMahine = CoffeeMachine()

    for i in range(7):
        try:
            print(coffeMahine.serve(bv.Coffee()))
            print(coffeMahine.serve(bv.Tea()))
            print(coffeMahine.serve(bv.Cappuccino()))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
        if coffeMahine.breaks == True:
            coffeMahine.repair()

if __name__ == '__main__':
    try:
        machine()
    except Exception as e:
        print(e)