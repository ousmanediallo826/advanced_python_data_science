#=====================1. The Foundations (Beginner)========================

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


    def bark(self):
        return  f"{self.name} say Woof"


dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "Husky")

print(dog1.bark())
print(dog2.bark())



#=====================2. The Four Pillars of OOP (Intermediate)================================

#====I. Encapsulation (Data Hiding)=======
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance


    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


account1 = BankAccount("Buddy", 100)
account2 = BankAccount("Luna", 200)
print(account1.get_balance())
print(account2.get_balance())
print(account1.deposit(100))
print(account2.deposit(200))
print(account1.get_balance())
print(account2.get_balance())


#======II. Abstraction (Hiding Complexity)========
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Ignition turned, pistons moving, engine purring."


#============III. Inheritance (Reusability)========
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language



#======IV. Polymorphism (Many Forms)=============

class AudioFile:
    def play(self): pass

class MP3File(AudioFile):
    def play(self): return "Decoding MP3 stream..."

class WAVFile(AudioFile):
    def play(self): return "Decoding WAV stream..."

def media_player(audio_object):
    print(audio_object.play())



#========================3. Advanced OOP Architecture====================
#===Multiple Inheritance & MRO (Method Resolution Order)===

class A:
    def texture(self): return "Smooth"
class B:
    def texture(self): return "Rough " + super().texture()

class C(A):
    def texture(self): return "Sticky " + super().texture()
class D(B, C):
    pass

print(D.__mro__)


#=====Descriptors=====
class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if value < 0: raise ValueError("Cannot be negative")
        instance.__dict__[self.name] = value

class Product:
    price  = Validator()



#===Part 1: State & Access Control====
class Thermostat:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        """Getter: Simply returns the internal hidden value."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter: Enforces boundaries before changing the data."""
        if value < -273.15: raise ValueError("Temperature below absolute zero is impossible!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Dynamic Property: Calculated on-the-fly without storing state."""
        return (self.celsius * 9 / 5) + 32

device = Thermostat(90)
print(device.celsius)
print(device.fahrenheit)

device.celsius = 35


#====2. dataclass (The Boilerplate Eliminator)===
from dataclasses import dataclass, field
@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    inventory: list = field(default_factory=list, init=False)

p1 = Product("Laptop", 999.99, 2)
p2 = Product("Laptop", 999.99, 2)

print(p1)
print(p1 == p2)
