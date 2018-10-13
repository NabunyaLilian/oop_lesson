from models.animal import Animal

class Dog(Animal):
    def __init__(self, name, gender, age, breed, color):
        super(Dog, self).__init__(name, gender, age)
        self.breed = breed
        self.color = color

    def make_sound(self):
        print("Bark Bark  ... ")


