#Base class
class Account:
    """This is the base Account class that has withdraw, deposit and commit methods""" #Doc string

    def __init__(self,filepath):    #Constructor function
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amount):    #Member method
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# account = Account("account/balance.txt")
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
# account.deposit(200)
# print(account.balance)
# account.commit()

#Sub class
class Checking(Account):
    """This class generates checking account objects"""

    type = "Checking"  #class variable

    def __init__(self, filepath):
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance = self.balance - amount

checking = Checking("account/balance.txt")    #Object instance or instantiation
checking.transfer(50)
print(checking.balance)
checking.commit()
