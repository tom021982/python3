class Bike:

    def setValues(self, price, speed, capacity):
        self.price = price
        self.speed = speed
        self.capacity = capacity

    def printValues(self):
        print("""Price: {0!s} Speed:{1!s} Capacity: {2!s} """.format(self.price, self.speed, self.capacity))

class MotorCycle(Bike):
    print("A Two Wheeler")

pulsar = Bike()
pulsar.setValues(80000, 190, 350)
pulsar.printValues()
