class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."

class Intern:
    def __init__(self, Name="My name? I’m nobody, an intern, I have no name."):
        self.Name = Name
    def __str__(self):
        return self.Name
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    def make_coffee(self):
        return Coffee()

def intern_madness():
    nobody = Intern()
    Mark = Intern("Mark")
    print(nobody.Name)
    print(Mark.Name)

    Mark_s_coffee = Mark.make_coffee()
    print(Mark_s_coffee)

    nobody.work()


if __name__ == '__main__':
    try:
        intern_madness()
    except Exception as e:
        print(e)