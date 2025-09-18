#Kady Manecha
'''''

larger_num = int(input("enter the larger number: "))
smaller_num = int(input("enter the smllest number:"))

num = 0
while larger_num > smaller_num:
    larger_num /= 2
    num += 1

print(f"Number of times halved: {num} ")

#2

word = input("enter a word: ")
result = ""
# First start point, Ending point, Step 
for i in range(1 , len(word) - 1,2):
    result += word[i]

print(f"output = {result}")

'''''
#3
for i in range(38, 1051, 2):
    print(i)