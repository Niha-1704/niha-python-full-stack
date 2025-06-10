from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

bike = Bike()
bike.start_engine()