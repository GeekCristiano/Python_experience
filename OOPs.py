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
