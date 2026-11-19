
from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    def calculate_year(self):
        return 2025 - self.joining_year

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Role: {self.role()}\n"
                f"Years on platform: {self.calculate_year()}")


class Customer(User):

    def role(self):
        return "Customer"


class Vendor(User):

    def role(self):
        return "Vendor"


user1 = Customer("Abhi", 2020)
user2 = Vendor("Raj", 2018)

print(user1)
print()
print(user2)
