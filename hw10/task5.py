class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None
    def get_spec(self):
        return self.spec


class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec



class Fish(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Bird(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self. spec = spec


if __name__ == '__mane__':

    dog_1 = Dog('Jack', 2, 'Поет')
    fish_1 = Fish('Nemo', 1, 'Плавает')
    bird_1 = Bird('Popka', 4, 'Плохо летает')



