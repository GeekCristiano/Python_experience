#  Let's learn how works object oriented programming in python

class car():

    def drive(self, speed):
        print("The car goes at a speed of %s km per hour." % speed)

    def stop(self):
        print("Car stops.")


car = car()
car.drive("50")
car.stop()