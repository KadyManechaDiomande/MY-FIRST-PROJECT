#Write code to determine how many leter are in a word
'''''
word = "hello world"

count = 0

for letter in word:
    if letter != " ":
        count += 1
print(count)

# Write code to determine how many vowel are in a givzen word
#aeiou

word = "hello world"
vowel = "aeiouy"

count = 0

for letter in word:
    if letter in vowel:
        count += 1
print('number of vowel:', count)
'''
#word2 = apples and bananas
#word3 = happy times
'''''
word1 = input()


vowel = "aeiouy"
count = 0

for letter in word1:
    if letter in vowel:
        count += 1
print(f"the vowel count in{word1} is

'''
'''''
#print("apple")
#mavpass

word = input("enter a word:")
for i in range (1, len(word), 2):
    print(word[i])
'''
'''''
larger = int(input("Enter the larger number: "))
smaller = int(input("Enter the smaller number: "))

count = 0
current = larger

while current > smaller:
    current /= 2
    if current > smaller:
        count += 1

print("Result:", count)
'''

'''''
word = input("Enter a word: ")   # Step 1: get word input

result = ""                      # Step 2: prepare empty result string

for i in range(1, len(word), 2): # Step 3: loop through every 2nd index (starting at 1)
    result += word[i]            # Step 4: add the letter to result

print("Result:", result)
'''''

for number in range(37, 1051, 2):  # Step 1: start at 38, go up by 2 until 1050
    print(number)          