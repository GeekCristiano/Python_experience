#  Let's learn how works object oriented programming in python

class car():
    def drive(self, speed):
        print("The car goes at a speed of %s km per hour." % speed)

    def stop(self):
        print("Car stops.")


mycar = car()
mycar.drive("50")
mycar.stop()


# inheritance example
class jaguarCar(car):
    def sound(self):
        print("bep-bep")

    def stop(self):
        print("Jaguar stops.")


jaguarCar = jaguarCar()
jaguarCar.drive("140")
jaguarCar.stop()
jaguarCar.sound()


class User():
    # Constructor of object
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def printUser(self):
        print("My name: %s" % self.name)
        print("I am %d years old" % self.age)

user= User("Bob", 27)
user.printUser()