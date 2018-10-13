class Animal:
    kingdom = "animalia"
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def say_my_name(self):
        print("My name is {} and I am {} years old".format(self.name, self.age))
