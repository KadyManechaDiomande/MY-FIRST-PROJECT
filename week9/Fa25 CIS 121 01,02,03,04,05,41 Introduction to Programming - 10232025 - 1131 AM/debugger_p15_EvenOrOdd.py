from random import randint  #introduit import randin

def guess(guess="even"):   #change odd to even
	value = randint(0, 9)
	
	if value // 2 == 0:   #modulos
		actual = "even"
	else:
		actual = "odd"
	
	if guess == actual:
		return "Correct!"
	else:
		return "Incorrect!"
	
print("\nFinal result: "+guess())
print(40*"_")
	