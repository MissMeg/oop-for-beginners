class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} old."

# Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        # calling the __init__ of the superclass (Animal)
        super().__init__(name, age)
        self.breed = breed

    # redefining a method from it's parent class
    def __str__(self):
        return f"{self.name} is {self.age} old and of breed {self.breed}."


# Cat also inherits from animal!
class Cat(Animal):
    def __init__(self, name, age):
        # calling the __init__ of the superclass (Animal)
        super().__init__(name, age)

    # new method
    def meows(self):
        return f"{self.name} says: MEOW!"

# instantiate a dog
jethro = Dog('Jethro', '6 months', 'Australian Shepherd')
print(jethro)

# instantiate a cat
tom = Cat('Tom', '5 months')
print(tom)