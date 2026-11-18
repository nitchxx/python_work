class Accounts :
    def __init__(self,_account_holder_name,_balance):
       self._account_holder_name = _account_holder_name
       self._balance = _balance

    def __add__(self, other):
        return self._balance + other._balance

class SavingsAccount(Accounts) :
    def Current_interest(self) :
        return self._balance * 0.05 

class Currentaccount(Accounts) :
   def Current_interest(self) :
           return self._balance * 0.02

user1 = SavingsAccount("Ravi",10000)
user2 = Currentaccount("Anjali",15000)

print("Account holder name : ",user1._account_holder_name," ","Balance : ",user1._balance," ","interest : ",user1.Current_interest())
print("Account holder name : ",user2._account_holder_name," ","Balance : ",user2._balance," ","interest : ",user2.Current_interest())
print("Total balance : ",user1+user2)