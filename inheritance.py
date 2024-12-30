class Animal:
    def __init__(self, name):
        self.name= name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        

#inheritance 
class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")
        
class Mouse(Animal):
    pass

dog = Dog("Scobby")
cat = Cat("Garfield")

dog.speak()

print(dog.name)