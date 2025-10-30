class planet:
    def __init__(self, name):
        self.name = name


import math
def my_fctn(value):
    print(value)

my_fctn('hello world')

planet1 = planet("x25")

class planet:
    def __init__(self, _name, _radius, _mass, _distance ):
        self.name = _name
        self.radius = _radius
        self.mass = _mass
        self.distance = _distance
    def get_name(self):
        return self.name
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_distance(self):
        return self.distance

planet1 = planet('X25', 45, 198, 1000 )
planet2 = planet('a37', 234, 2381)

print(planet1.get_mass())
print(planet2.get_volume())


