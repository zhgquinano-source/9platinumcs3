#Questions:

#What is duck typing, as explained in the video?
#This means that if the object has the needed method, Python can use it regardless of what class it comes from.

#What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
#To work inside the same loop as Dog and Cat, the Car class needs to have the same method name that the loop calls. Python's duck typing checks for behavior rather than class inheritance.


#How does the code in 2.2 demonstrate polymorphism?
#The code demonstrates polymorphism (duck typing) because start_trip() accepts objects from unrelated classes (Car, Boat, and Drone). As long as each class implements the move() method, the function executes it based on behavior rather than class type.

Actual Code:
class Car: # created a class for Car
    def move(self): # Method of Car
        print("The car drives on the road.")

class Boat: # created a class for Boat
    def move(self): # Method of Boat
        print("The boat sails on water.")

class Drone: # created a class for Drone
    def move(self): # Method of Drone
        print("The drone flies in the sky.")

def start_trip(vehicle): # Function that takes a vehicle parameter and calls its move() method
    vehicle.move()

# Creates an object for each class
Car = Car()
Boat = Boat()
Drone = Drone()

# Calling the start_trip() method for each object
start_trip(Car)
start_trip(Boat)
start_trip(Drone)
