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
'''''
#3
for i in range(38, 1051, 2):
    print(i)
'''

#4
word = ""

# whileloop that runs forever
while True:
    #Read the user input
    user_in = input("Enter a letter:")
    # If the user typed "done" we stop !
    if user_in == "done":
        break
    else:
        # Else lets add letter into the word
        word += user_in

#print out the final word
print(f"The final word is{word}")

#5

start = 50
end = 517

# Assume 50-517 Inclusive

# Start with 51 and stop before 518, take steps pf 2
for i in range(start + 1, end + 1, end + 1, 2):
    print(i)
    trhth