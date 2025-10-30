import math
class Planet:



class Star:


'''Create a planetary system class that take a star as an argument, has the ability 
to add planet to the system, and can print all the planet in the system'''

class PlanetarySystem:
    def __init__(self, _star):
        self.star = _star
        self.planet = []

    def add_planet(self, _planet):
        self.planets.append(_planet)

    def show_planets(self):
        '''iterate through each planet and print the name'''
        for planet in planets:
            print(planet.get_name())
    