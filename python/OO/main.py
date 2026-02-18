class animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class dog(animal):
    pass

animal1 = animal('bicho 1')

animal2 = dog('bicho 2')

print(animal1)
print(animal2)
