#13/11/2025
#6

class RationalNumber:
    def __init__(self, _numerator = 1, _denominator = 1):
        self.a = _numerator
        self.b = _denominator

    def __add__(self, other_fraction):
        new_numerator = 0
        new_denominator =0
      #if the denominator is the same!'
        if self.denominator == other_fraction.denominator:
            new_numerator = self.numerator + other_fraction.numerator
            new_denominator = self.denominator
        else:
            'if denominator is different , calculate new denominator'
            new_denominator = self.denominator * other_fraction.denominator
            '1/3 + 1/2'
            '2/6 + 3/6'
            '5/6'
            new_numerator = (self.numerator * other_fraction.denominator) +  (other_fraction.numerator * self.denominator)
        
        return RationalNumber(new_numerator, new_denominator)
    
    def __str__(self):
        return f"{self.numerator} / {self.denominator}"
    
fraction1 = RationalNumber(1, 3)
fraction2 = RationalNumber(1 , 2)
fraction3 = fraction1 + fraction2
print(fraction3)

#5
import math

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    
    def __str__(self):
        if self.b == 0:
            return f"{self.a}x"
        elif self.a == 0:
            return f"{self.b}y"
        else:
            return f"{self.a}x + {self.b}y" if self.b > 0 else f"{self.a}x - {-self.b}y"

vector1 = Vector(3, 4)
vector2 = Vector(3, 4)

print(vector1 == vector2)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

pt1 = Point(3, 4)
pt2 = Point(0, 0)
print(pt1 == pt2)
print(pt1)

class LinearEquation:
    def __init__(self, m, b):
        self.m = m
        self.b = b
    
    def __add__(self, other):
        return LinearEquation(self.m + other.m, self.b + other.b)
    
    def __str__(self):
        if self.m == 0:
            return f"y = {self.b}"
        elif self.m == 1:
            return f"y = x + {self.b}" if self.b != 0 else "y = x"
        elif self.m == -1:
            return f"y = -x + {self.b}" if self.b != 0 else "y = -x"
        else:
            return f"y = {self.m}x + {self.b}" if self.b != 0 else f"y = {self.m}x"

eq1 = LinearEquation(2, 3)
eq2 = LinearEquation(-1, 5)
eq3 = eq1 + eq2
print(eq1)

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        carry_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60
        return Time(self.hours + other.hours + carry_hours, remaining_minutes)
    
    def __str__(self):
        return f"{self.hours}h {self.minutes}m"

t1 = Time(1, 30)
t2 = Time(2, 45)
t3 = t1 + t2
print(t3)

class RGBColor:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __add__(self, other):
        return RGBColor(min(255, (self.r + other.r) // 2), min(255, (self.g + other.g) // 2), min(255, (self.b + other.b) // 2))
    
    def __str__(self):
        return f"RGB({self.r}, {self.g}, {self.b})"

c1 = RGBColor(170, 150, 200)
c2 = RGBColor(30, 100, 60)
c3 = c1 + c2
c4 = RGBColor(50, 50, 50)
c5 = c3 + c4
print(c5)

class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __add__(self, other):
        common_denom = self.denominator * other.denominator
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        return RationalNumber(new_num, common_denom)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

r1 = RationalNumber(1, 3)
r2 = RationalNumber(1, 2)
r3 = r1 + r2
print(r3)

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    
    def __str__(self):
        if self.b == 0:
            return f"{self.a}"
        elif self.a == 0:
            return f"{self.b}i" if self.b != 1 and self.b != -1 else ("i" if self.b == 1 else "-i")
        else:
            if self.b == 1:
                return f"{self.a} + i"
            elif self.b == -1:
                return f"{self.a} - i"
            else:
                return f"{self.a} + {self.b}i" if self.b > 0 else f"{self.a} - {-self.b}i"

z1 = ComplexNumber(3, 2)
z2 = ComplexNumber(-1, 4)
print(z1 == z2)
print(z1)

class Playlist:
    def __init__(self, name="New Playlist", songs=None):
        self.name = name
        self.songs = songs if songs else []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __add__(self, other):
        return Playlist(self.name, self.songs + other.songs)
    
    def __str__(self):
        return f"{self.name}: {self.songs}"

pl1 = Playlist("My Playlist")
pl1.add_song("Song A")
pl1.add_song("Song B")
pl2 = Playlist("Other Playlist")
pl2.add_song("Song C")
pl3 = pl1 + pl2
print(pl3)

class ShoppingCart:
    def __init__(self, items=None):
        self.items = items if items else {}
    
    def add_item(self, item):
        self.items[item] = self.items.get(item, 0) + 1
    
    def __add__(self, other):
        result = ShoppingCart(self.items.copy())
        for item, qty in other.items.items():
            result.items[item] = result.items.get(item, 0) + qty
        return result
    
    def __str__(self):
        return str(self.items)

cart1 = ShoppingCart()
cart1.add_item("tea")
cart1.add_item("energy drink")
cart1.add_item("energy drink")
cart2 = ShoppingCart()
cart2.add_item("energy drink")
cart2.add_item("hat")
cart3 = cart1 + cart2
print(cart3)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __mul__(self, other):
        return Rectangle(self.width * other, self.height * other)
    
    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"

rect1 = Rectangle(4, 5)
rect2 = rect1 * 3
print(rect2)