# Creates the Parent class
class Animal:
    def __init__(self, name): # Creates the property of the Parent Class
        self.name = name

    # Creates the methods of the Parent Class
    def make_sound(self):
        print(f"{self.name}, makes a sound".) # method to output what sound the animal makes
  
    def eat(self):
        print(f"{self.name}, eats".) # method to output that the animal eats

# Child Class No. 1
class Lion(Animal): # Creates a Child Class from the Parent Class Animal
    def __init__(self, name):
        super().__init__(name) # Makes sure that it inherits from the Parent Class

    # These new methods overrides the original methods in the Parent Class
    def make_sound(self): 
        return f"{self.name} roars loudly!" # This is where we will use overriding methods, it will not output "_ makes a sound", instead it outputs "_ roars loudly!"

    def eat(self):
        return f"{self.name} eats fresh meat." # Outputs " _ eats fresh meat" instead of "_ eats"

# Child Class No. 2
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"{self.name} trumpets!"                    # Same with this class

    def eat(self):
        return f"{self.name} eats grass and fruits."

# Child Class No. 3
class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"{self.name} chatters!"                    # And this class

    def eat(self):
        return f"{self.name} eats bananas."

#Creates the Object Class
lion = Lion("Simba") # Object for lion named "Simba"
elephant = Elephant("Dumbo") # Object for elephant named "Dumbo"
monkey = Monkey("George") # Object for monkey named "George"

# By using a for loop this Outputs the methods of the Animals one by one 
for animal in animals:
    print(animal.make_sound())
    print(animal.eat())
    print("-----")
