
class Pet:
    def __init__(self, owner):
        self._owner = owner

    @property
    def owner(self):
        return self._owner

class Animal:
    def move(self):
        print("moving on...")

class Dog(Animal):
    def bark(self):
        print("woof woof")

class PetDog(Pet, Dog):
    pass

pd = PetDog('John')

print(pd)
print(pd.owner)
pd.move()
pd.bark()

print(PetDog.mro())