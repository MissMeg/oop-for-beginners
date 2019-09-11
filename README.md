# Object Oriented Python Guide

The idea behind Object Oriented Python, or OOP, is to create DRY (Don't Repeat Yourself) code by organizing them in objects. Objects have two characteristics, attributes and behavior.

For example, a dog is an object while name, age, and color are attributes and eating, barking, and playing are behaviors.

## Class

A `class` is the structure for the object.

Let's look at this in a code example:

```python
class Dog:
    pass
```

The `class` keyword define the empty class `Dog`.

## Instance

An *instance* is an instantiation of a class. (Clears that right up doesn't it :joy:) This means that you have created an object that is structured or defined by the `class` you created. No memory or storage is used when this happens. :+1:

```python
class Dog:
    pass

dog_instance = Dog()
```

In this code snippet, `dog_instance` is an object of the class `Dog`.

## Attributes

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

# let's change their class attribute
jethro.can_fly = True
print(jethro.can_fly)
print(luna.can_fly)
> True
> False

# let's change their instance attribute
print(jethro.age)
> '6 months'
jethro.age = '7 months'
print(jethro.age)
> '7 months'
```

### Quiz Time #1

Post your answers to this quiz as comments on [this issue](https://github.com/MissMeg/oop-practice/issues/1).

1) What is a `class`?
2) What is an instance?
3) What is the difference between a class attribute and an instance attribute?
4) Create your own class with a class attribute and an instance attribute.

## Methods

## Inheritance

## Encapsulation

## Polymorphism
