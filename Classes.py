#Constructors:
class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f"Hi, I am {self.name}")



john = Person("JOhn Smith")
print(john.name)
john.talk()
bob = Person("MAdan Lal")
print(bob.name)
bob.talk()


#Inheritence:
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

cat1 = Cat()
cat1.be_annoying()
dog1 = Dog()
dog1.walk()

