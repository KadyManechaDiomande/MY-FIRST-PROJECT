
from math import sqrt
class Vector:
	def __init__(self, x_direction, y_direction): #include self
		self.x_direction = x_direction
		self.y_direction = y_direction
	
	def get_x_direction(self):
		return self.x_direction   # y should be x
	
	def set_x_direction(self, x_direction):
		self.x_direction = x_direction
	
	def get_y_direction(self):
		return self.y_direction
	
	def set_y_direction(self, y_direction):
		self.y_direction = y_direction
	
	def get_magnitude(self):
		return sqrt(self.x_direction**2 + self.y_direction**2)  #import sqrt
	
v = Vector(3, 4)
print(v.get_x_direction())
