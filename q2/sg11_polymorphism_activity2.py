#Questions:
#What is duck typing, as explained in the video?

#What did the Car class need to have so it could work inside the same loop as Dog and
#Cat, even if it does not inherit from the Animal class?

#Does the code in 2.2 demonstrate polymorphism?


Actual Code:
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The boat sails on water.")

def start_trip(vehicle):
    vehicle.move()
  
Car = Car()
Boat = Boat()
Drone = Drone()

start_trip(Car)
start_trip(Boat)
start_trip(Drone)
