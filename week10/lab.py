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
    
    #get price in Canadian dollars:
    def get_price_cad(self):
        return sef.price * 1.40
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
apple_watch = Product("Apple watch series7", 499)
#set the product price
print(apple_iphone)
print(apple_watch)
#create the product quantity
apple_watch.set_quantity(5)
apple_iphone.set_quantity(5)
#Print product
print(apple_watch)
print(apple_iphone)



#2
class Book:
    def __init__(self, input_title, input_author):
       #private class varables
        self.title = input_title
        self.author = input_author
        self.page_count = 0

    def get_page_count (self):
        return self.page_count
    def set_page_count (self, value):
        if value > 0:
            self.page_count = value
    def __str__ (self):
        return f"The book is {self.title} and author is {self.author} it has {self.page_count} pages."
book1 = set_page_count(328)
book2 = set_page_count(180)

print(book1)
print(book2)

#6
class Statement:
    def __init__(self)
        self.name ="Unknown"
        self.major = "Unknown"
        self.gpa = 0

        def get_name (self):
            return self.name
        def set_name (self, value):
            self.name = value

        def get_major(self):
            return self.major
        def set_major(self, value):
            self.major = value

        def get_gpa(self):
            return self.gpa
        def set_gpa(self, value):
            if 0 <= value <= 4.0:
                self.gpa = value

        def introduce(self):
            return f"Hi , i am {self.name}. I'm studying {self.major}."
        def study_for_xam(self):
            if self.gpa < 4.0:
                self.gpa += 0.2
student1 = Student()
student1.set_name("Evan Linder")
student1.set_major("Computer Science")
student1.set_gpa(3.2)
student1.study_for_exam()

print(student1.introduce())
print(student1.get_gpa())


#7
class Vehicle:
    def __init__(self):
        self.make = "Unknown"
        self.model = "Unknown"
        self.year = 0

    def get_make(self):
        return self.make
    def set_make(self, value):
        self.make = value

    def get_model(self):
        return self.model
    def set_model(self, value):
        self.model = value

    def get_year(self):
        return self.year
    def set_year(self, value):
        if value > 0:
            self.year = value
   
    def print_vehicle_type(self):
        return f"{self.year} {self.make} {self.model}"
            
            
        
        

    
    

        
    
    
