class Dog:
    legs = 4
    ears = 2
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed
dogs=Dog("Rory", "golden retriver")
dim=Dog("Larry", "Chiwawa")
print(dogs.name, dogs.breed, dogs.legs, dogs.ears, dim.name, dim.breed, dim.legs, dim.ears)    