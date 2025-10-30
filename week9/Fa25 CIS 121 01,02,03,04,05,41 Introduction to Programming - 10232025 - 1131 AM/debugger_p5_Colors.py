class ColorRGB:
	def __init__(self, red, green, blue):  #self
		self.red = red
		self.green = green
		self.blue = blue
	
	def get_red(self):
		return self.red
	
	def set_red(self, red):
		self.red = red
	
	def get_green(self):
		return self.green
	
	def set_green(self, green):
		self.green = green      #self reverse
	
	def get_blue(self):
		return self.blue
	
	def set_blue(self, blue):  # remove this def
		self.blue = blue
	
	def to_grayscale(self):
		return 0.5 * self.red + 0.59 * self.green + 0.11 * self.blue
c = ColorRGB(100, 150, 200)
print(c.get_green())
c.set_green(180)
print(c.get_green())
print(c.to_grayscale())