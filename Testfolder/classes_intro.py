class Person:
    def __init__(self, age, name):
        self.__age = age
        self.name = name

    def birthday(self):
        self.__age += 1

    # @property
    # def age(self):
    #     return self.__age

    @age.setter
    def age(self, value: int):  # checking for ints at compiletime.
        if value >= 0 and value <= 125:
            self.__age = value


p1 = Person(41, "Anders")
p2 = Person(39, "Lars")
p3 = Person(12, "Sunniva")
