def find_factors(num):
	factors = []
	
	for i in range(1, num + 1):  #nu; should be num+1
		if num % i == 0:  #change != to ==
			factors.append(i)  #append au lieu  de add

	return factors
print(find_factors(12))