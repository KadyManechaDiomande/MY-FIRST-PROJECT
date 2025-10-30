def return_unique(numbers):

	number_dicitonary = {}
	#load dictionary
	for number in numbers:  #change range(len(number)) to numbers
		if number in number_dicitonary:
			number_dicitonary[number] += 1	#change =1 to +=1		
		else:
			number_dicitonary[number] = 1  #change += to =

	unique_numbers = []
	#find unique numbers in dictionary
	for number in number_dicitonary:   #remove .values
		if number_dicitonary[number] == 1:
			unique_numbers.append(number)

	return unique_numbers
print(return_unique([1,2,2,3,4,4,5]))