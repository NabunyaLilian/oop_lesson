from models.animal import Animal

class Cat(Animal):
    def __init__(self, name, gender, age, color, eyes):
        super(Cat, self).__init__(name, gender, age)
        self.color = color
        self.eyes = eyes

    def make_sound(self):
        print("Meow Meow .... :)")