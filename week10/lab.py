#2025/10/30

#1
class Product:
    
    #this will run first as we create the class
    def __init__(self, input_name, input_price):
       #private class varables
        self.name = input_name
        self.price = input_price
        self.quantity = 0
#get method
    def get_price(self):
        return self.price
    #set method
    def set_price(self, value):
        if value > 0:
            self.price = value

    #get method
    def get_quantity(self):
        return self.quantity
    #set method
    def set_quantity(self, value):
        if 0 <= value <99:
            self.quantity = value
        else:
            raise ValueError
    
    #Build in print method
    def __str__(self):
        return f"The product is {self.name} and priced at {self.price} we have {self.quantity}"

#create the product with name
apple_iphone = Product("Iphone 17 pro Max", 1499)
apple_watch = Product("Apple Zatch series7", 499)
#set the product price
print(apple_iphone)
print(apple_watch)
#create the product quantity
apple_watch.set_quantity(5)
apple_iphone.set_quantity(5)
#Print product
print(apple_watch)
print(apple_iphone)



#