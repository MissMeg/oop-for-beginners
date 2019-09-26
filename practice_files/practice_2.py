class Dog:
    # class attributes
    num_of_legs = 4
    can_fly = False

    # instance attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # instance method
    def sing(self):
        print(f"{self.name} sings the song of her people.")

    def fetch(self, item):
        print(f"{self.name} runs to fetch the {item}.")

    def __str__(self):
        return f"{self.name} is {self.age} old."

jethro = Dog('Jethro', '6 months', 'Australian Shepherd')
luna = Dog('Luna', '4 months', 'Labrador Retreiver')

# calling instances methods
print("----Calling Methods----")
jethro.sing()
luna.fetch("ball")

# calling print
print("----Calling Print----")
print(jethro)