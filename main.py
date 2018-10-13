from models.animal import Animal
from models.cat import Cat
from models.dog import Dog

def root():
    my_animal = Animal("Fire fox", "Female", 23)
    my_animal.say_my_name()

    bootsyCallaco = Cat("Bootsy Callaco", "male", 12, "yellow", "BIG")
    scoobyDoo = Dog("Scooby Doo", "male", 50, "German Shepherd", "browny")

    bootsyCallaco.make_sound()
    scoobyDoo.make_sound()

    bootsyCallaco.say_my_name()
    scoobyDoo.say_my_name()


if __name__ == '__main__':
    root()
