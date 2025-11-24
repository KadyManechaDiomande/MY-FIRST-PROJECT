class Dog:
    def __init__(self, _name, _size, _breed = "Unknown") :
        self.name = _name 
        self.size = _size
        self.breed = _breed

    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    def get_breed(self):
        return self.breed
    

    def set_name(self, new_name):
        self.name = new_name
    def set_size(self, new_size):
        self.size = new_size
    def speak(self):
        """Small ogs = yip / medium dogs = bark / large dogs = bow wow"""
        if self.size == 1:
            print("yip")
        elif self.size ==2:
            print("bark")
        elif self.size ==3:
            print("bow wow")





class DogPark:
    def __init__(self, _name):
        self.name = _name
        self.dogs = []
    def add_dog(self, dog):
        self.dogs.append(dog)
    def show_dogs(self):
        for dog in self.dogs:
            print(dog.get_name())
    def change_dog_name(self, old_name, new_name):
        for dog in self.dogs:
            if dog.get_name() == old_name:
                dog.set_name(new_name)
    def find_dog(self, dog_name):
        for dog in self.dogs:
            if dog.get_name() == dog_name:
                dog.speak()
    def call_dog(self, dog_name):
        """this is calls the gods and removes it from the park"""
        for dog in self.dogs:
            if dog.get_name()== dog_name:
                self.dogs.remove(dog)


park1 = DogPark("Bark Zone")

#dog1 = Dog("Spoot", 2, "lab")
#park1.add_dog(dog1)

#dog2 = Dog("Rover", 3, "Mastiff")
#park1.add_dog(dog2)

park1.add_dog(Dog("Spot", 2, "lab"))
park1.add_dog(Dog("Rover" 3, "Mastiff"))
park1.add_dog("Fluffy", 1)

#park1.show_dogs()
park1.change_dog_name("Spoot", "Spot")
#park1.show_dogs()
park1.find_dog("Rover")

            


#6/11/25
    #write a class for a bank account .
    #Bank account should have an ozner and a balance, and should be able to 
    #Deposit
    #Withdraw money


class Bankaccount
def __init__(self,name, initial_balance = 0):
    self.owner = name
    self.balance = initial_balance

def deposit(self, value):
    self.balance += value
def withdraw(self, value):
    if value > self.balance:
        print(f"here is your ${value}.")
        self.balance -= value
def get_balance(self):
    return self.balance
def get_owner(self):
    return self.owner
def set_owner(self, new_owner):
    self.owner = new_owner

def __add__(self, other):
    new_owner = f'{self.get_owner()} & {other.get_owner()}'
    new_balance = self.getr_balance() + other.get_balance()
    #new_account = f'owner: {new_owner}, balance: {new_balance}'
    new_account = BankAccount(new_owner, new_balance)
    return new_account

def __eq__(self, other):
    #assume at this bank, you can only have one account
    #that means, if the owner names are the same, then it is the same account 
    return self.

matt_acc = BankAccount("Matt")
matt_acc.deposit(100)
matt_acc.deposit(50)
#matt_acc.withdraw(250)
#print(matt_acc.get_balance())


#ashley_acc = BankAccount("Ashley", 500)
#ashley_acc.deposit(250)


join_acc = matt_acc + ashley_acc
print 
