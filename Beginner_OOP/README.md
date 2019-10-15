# Object Oriented Python Guide

The idea behind Object Oriented Python, or OOP, is to create DRY (Don't Repeat Yourself) code by organizing them in objects.

Objects have two characteristics, attributes and behavior. For example, a dog is an object while name, age, and color are attributes and eating, barking, and playing are behaviors.

## Section 1

### Class

A `class` is the structure for the object.

Let's look at this in a code example:

```python
class Dog:
    pass
```

The `class` keyword define the empty class `Dog`.

### Instance

An *instance* is an instantiation of a class. (Clears that right up doesn't it :joy:) This means that you have created an object that is structured or defined by the `class` you created. No memory or storage is used when this happens. :+1:

```python
class Dog:
    pass

dog_instance = Dog()
```

In this code snippet, `dog_instance` is an object of the class `Dog`. Each instance gets its own memory address so no two instances will be the same even with the same info.

```python
class Dog:
    pass

dog_instance1 = Dog()
dog_instance2 = Dog()
print(dog_instance1 == dog_instance2)
> FALSE
```

If you ever need to figure out an object's class, call the `type()` function.

```python
class Dog:
    pass

dog_instance1 = Dog()
type(dog_instance1)
> <class '__main__.Dog'>
```

Both instances will have the same type:

```python
class Dog:
    pass

dog_instance1 = Dog()
dog_instance2 = Dog()
type(dog_instance1) == type(dog_instance2)
> TRUE
```

### Attributes

When adding attributes, you can create them for the class or the instance. Class attributes as shared across all instances of the class. Instance attributes are set when an instance is created and is unique to each instance.

```python
class Dog:
    # class attributes
    num_of_legs = 4
    can_fly = False
```

In order to set instance attributes, we need to include them when the instance is created or initialized. We do this by creating a function called `__init__` inside of the class. Let's look at an example:

```python
class Dog:
    # class attributes
    num_of_legs = 4
    can_fly = False

    # instance attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
```

Let's break down what was added in this last code snippet. `self` refers to the instance of the object itself. Essentially, you are saving the passed variables (name, age, breed) to the instance.

Let's create some instances and do some printing to the console:

```python
class Dog:
    # class attributes
    num_of_legs = 4
    can_fly = False

    # instance attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

jethro = Dog('Jethro', '6 months', 'Australian Shepherd')
luna = Dog('Luna', '4 months', 'Labrador Retreiver')

# both will be 4 because it is a shared class attribute
print(jethro.num_of_legs)
print(luna.num_of_legs)
> 4
> 4

# now these will be different because they are instance attributes
# each instance will have to set these
print(jethro.name)
print(luna.name)
> 'Jethro'
> 'Luna'
```

In order to access the attributes, you will need to use dot notation like this: `jethro.breed`. To reiterate, class attributes will be the same for every instance, but instance attributes will be unique each time you create an object.

How do you change an attribute? You change it just like any other variable in Python :snake:

```python
class Dog:
    # class attributes
    num_of_legs = 4
    can_fly = False

    # instance attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

jethro = Dog('Jethro', '6 months', 'Australian Shepherd')
luna = Dog('Luna', '4 months', 'Labrador Retreiver')

# let's change a class attribute
jethro.can_fly = True
print(jethro.can_fly)
print(luna.can_fly)
> True
> False

# let's change an instance attribute
print(jethro.age)
> '6 months'
jethro.age = '7 months'
print(jethro.age)
> '7 months'
```

#### Quiz Time #1

Post your answers to this quiz as comments on [this issue](https://github.com/MissMeg/oop-practice/issues/1) and I will check them out! *If you need to play around with some code first, check out the [practice_1.py file](https://github.com/MissMeg/oop-practice/blob/master/practice_files/practice_1.py) for the code used here in the examples that you can run in your own IDE to practice and play around with.*

1) What is a class?
2) What is an instance?
3) What is the difference between a class attribute and an instance attribute?
4) Create your own class with a class attribute and an instance attribute.

## Section 2

### Methods

Methods are functions inside of a class. They define the behaviors of the object.

```python
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


# instantiate the object
jethro = Dog('Jethro', '6 months', 'Australian Shepherd')
luna = Dog('Luna', '4 months', 'Labrador Retreiver')

# call our instance methods
jethro.sing()
luna.fetch("ball")
> "Jethro sings the song of her people."
> "Luna runs to fetch the ball."
```

The two methods that were created above are called instance methods because they are called on an instance object.

One thing to keep in mind when working with classes is what happens when you try to use common functions like `print()`. For example:

```python
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


# instantiate the object
jethro = Dog('Jethro', '6 months', 'Australian Shepherd')
luna = Dog('Luna', '4 months', 'Labrador Retreiver')

# trying the print method
print(jethro)
> <__main__.Dog object at 0x00aeff70>
```

In order to have the `print()` function print out something to the screen instead of this object message, you will need to add a special instance method called `.__str__()`. These are typically called **dunder methods** because they begin with double underscores.

```python
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
        return f"{self.name} sings the song of her people."

    def fetch(self, item):
        return f"{self.name} runs to fetch the {item}."

    def __str__(self):
        return f"{self.name} is {self.age} old."


# instantiate the object
jethro = Dog('Jethro', '6 months', 'Australian Shepherd')
luna = Dog('Luna', '4 months', 'Labrador Retreiver')

# now the print method works
print(jethro)
> "Jethro is 6 months old."
```

***
**Tip:** *Don't worry about trying to memorize all of the dunder methods out there because there are a lot! This is an area developers typically go to the docs to check for the dunder method they need.*
***

#### Quiz Time #2

Post your answers to this quiz as comments on [this issue](https://github.com/MissMeg/oop-practice/issues/2) and I will check them out! *If you need to play around with some code first, check out the [practice_2.py file](https://github.com/MissMeg/oop-practice/blob/master/practice_files/practice_2.py) for the code used here in the examples that you can run in your own IDE to practice and play around with.*

1) What is a method?
2) Add two methods to the class you created previously. The first shouldn't need any arguments (like `.sing()`) and the second should take at least 1 argument (like `.fetch("ball")`).
3) Use the `__str__()` dunder method to be able to print an instance of your class to the console. (like `print(jethro)`)
4) Review: Create another class with class attributes, instance attributes, methods, and a dunder method. Try to create something different than your first class. For instance, if you created a different animal for your first class, then maybe try creating a car class here.

## Section 3

### Inheritance

Inheritance is where one class (child class) takes on attributes and methods of another class (parent class).

This is where OOP can get a little messy...

Child classes can override and extend parent classes which means a child class inherits all of the parent's attributes and methods but can also specify it's own attributes and methods that are unique to themselves. Child classes can even redefine methods from their parent class.

***
**Python 3:** *In Python 3 a class implicitly uses `object` as the parent class. so the following is the same:*

```python
# class childClass(parentClass):
class Dog(object):
    pass

# is the same as

class Dog:
    pass
```

***

Inheritance can help a lot with code reuse, because the child classes can change specific methods and create new ones:

```python
# parent class
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
> "Jethro is 6 months old and of breed Australian Shepherd."

# instantiate a cat
tom = Cat('Tom', '5 months')
print(tom)
> "Tom is 5 months old."
```

### Encapsulation

Encapsulation is one of the crucial OOP concepts in which access to object methods and variables can be restricted.
The main goal is to avoid accidental changes. Furthermore, the methods can validate if the correct values are set otherwise return an error.

#### Encapsulation with Python

Despite the fact that Python does not have the `private` keyword like some other OOP languages,
encapsulation can be achieved.  

If you don't want to give direct access to a class variable, prefixing it with `__` will do the job. Here is an example:

```python
class Car(object):
    def __init__(self):
        self.make = 'Honda'
        self._model = 'Accord Sport'
        self.__vin = 'VINJH4TB2H26CC000000'

c = Car()
print(c.make)
print(c._model)
print(c.__vin)
```

Running the code above will return the following:

```python
Honda
Accord Sport
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3296, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-3-4d5dc80bbe38>", line 4, in <module>
    print(c.__vin)
AttributeError: 'Car' object has no attribute '__vin'
```

__Note:__ Although the `__` returned an error it is still accessible; however, it is harder to access.
Python has private variables by convention.

### Polymorphism

Polymorphism is when one function can be used in more than one way. For example:

```python
class Dog():
    def speak:
        print("Woof!")


class Cat():
    def speak:
        print("Meow!")
```

The two classes above have the same function `speak()` but the output is different. Polymorphism allows us to use similar syntax to work with different elements.
