class Animal:
    def walk(self):
        print("walk")


class Dog(Animal):
    pass


class Cat(Animal):
    def mews(self):
        print("mews")

    def walk(self):
        print("Cat walks")


cat1 = Cat()
cat1.mews()
cat1.walk()

dog1 = Dog()
dog1.walk()

animal = Animal()
animal.walk()
