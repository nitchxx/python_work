from abc import ABC, abstractmethod

class user(ABC):
    def __init__(self,name,account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        return 2025 - self.account_year

    @abstractmethod
    def get_role():
        pass


class Admin(user):
    def get_role(self):
        return "Admin"
    
    def __str__(self):
         return f"Welcome {self.name}! You are a valued {self.get_role()}."


class Guest(user):
    def get_role(self):
        return "Guest"
    
    def __str__(self):
         return f"Welcome {self.name}! You are a valued {self.get_role()}."

user1 = Admin("Abhi", 2020)
user2 = Guest("Raj", 2018)

user1 = Admin("Abhi", 2020)
user2 = Guest("Raj", 2018)

print("Role:", user1.get_role())
print("Account age:", user1.account_age())
print(user1)

print()

print("Role:", user2.get_role())
print("Account age:", user2.account_age())
print(user2)
