class Person:

    population = 0  # class variable

    def __init__(self, name):
        self.name = name
        print('Initializing %s' % self.name)

        Person.population += 1

    def __del__(self):
        print('%s say bye.' % self.name)

    def sayHi(self):
        print('Hi, my name is %s ' % self.name)

    def howMany(self):
        if Person.population == 1:
            print('I am the only person here.')
        else:
            print('We have %d persons here.' % Person.population)

Ganesh = Person('Ganesh')
Ganesh.sayHi()
Samrudhi = Person('Samrudhi')
Samrudhi.sayHi()
Ganesh.sayHi()
Ganesh.howMany()
