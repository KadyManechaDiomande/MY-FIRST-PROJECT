def hailstone_seq(n):
	sequence = [n] # change n/n to n
	
	while n != 1:
		if n % 2 == 0:
			n = n // 2
		else:
			n = 3 * n + 1  #2 should be 3
		sequence.append(n)   #change indent under else
		
	return sequence

print(hailstone_seq(6))