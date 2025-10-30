def hamming_distance(str1, str2):
	if len(str1) != len(str2):
		return "Strings must be of equal length."
	
	distance = 0  #change 1 to 0
	for i in range(len(str1)):   # remove -1 it should be full lenth
		if str1[i] != str2[i]:  #change to !=
			distance += 1
	return distance
print(hamming_distance("river", "rover"))