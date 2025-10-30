def design_rug(width, length, pattern):
	result = "Your rug is:\n"
	for i in range(length -1):
		result += pattern * width
		if i < length - 1:
			result += "\n"
	return result
print(design_rug(2,6,"@"))