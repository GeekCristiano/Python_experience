#  Let's learn how works object oriented programming in python

class car():
    def drive(self, speed):
        print("The car goes at a speed of %s km per hour." % speed)

    def stop(self):
        print("Car stops.")

# inheritance example
class jaguarCar(car):
    def sound(self):
        print("bep-bep")

    def stop(self):
        print("Jaguar stops.")

class User():
    # Constructor of object
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def printUser(self):
        print("My name: %s" % self.name)
        print("I am %d years old" % self.age)

    def __str__(self):
        return "User object"


def main():
    mycar = car()
    mycar.drive("50")
    mycar.stop()
    jaguarcar = jaguarCar()
    jaguarcar.drive("140")
    jaguarcar.stop()
    jaguarcar.sound()

    user= User("Bob", 27)
    user.printUser()
    print(user)

if __name__=="__main__":
    main()