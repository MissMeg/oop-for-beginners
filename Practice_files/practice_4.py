class Car(object):
    def __init__(self):
        self.make = 'Honda'
        self._model = 'Accord Sport'
        self.__vin = 'VINJH4TB2H26CC000000'

c = Car()
print(c.make)
print(c._model)
print(c.__vin)