class Player:

    def __init__(self, name):
        self.guy = name

    def askName(self):
        print('Hello, my name is', self.guy)

p = Player('Umesh Yadav')
p.askName()
