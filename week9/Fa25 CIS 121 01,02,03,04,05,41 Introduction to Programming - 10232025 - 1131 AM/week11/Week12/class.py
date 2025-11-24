#11/11/2025
#print('helllo world')
#Write a program that take integer from the user and adds them together 
#Until they type done. return the sum.
'''''
total = 0
    user_input = input("Enter an integer (or type 'done' to finish): ")
    
    While user_input != 'done':
        number = float(user_input)
        total += number
     user_input = input("Enter an integer (or type 'done' to finish): ")

print(f'total = {total}')
'''
'''''
#var_name = open('whatever your file name is . ext ','w')
#if filename does not exists at that path:
    #my_file = open('number.txt', 'w')
my_file = open('numbers.txt', 'w')

my_file.write('Hello world!\n')
my_file.write('Hello world!')


from random import randint
#var_name = open('whatever your file name is . ext ','w')
 new_file = open('number.txt', 'w')

for index in range(0,100):
    number = randint(50,250)
    my_file.write(f'{number}\n')
    #my_file.write(str(numbe)+'\n')

new_file.close()
'''
'''''
my_file = open("numbers.txt", "r")

data = my_file.readlines()

total = 0
count = 0

for line in data:
    number = float(line)
    total += number
    count += 1

print(f"total = {total}")
print(f'avg = {total/count}')
'''''


new_file = open('family.txt', 'w')

new_file.write('Name,age,occupation,hobby\n')
new_file.write('Matt,39,Teache,Running\n')
new_file.write('Dexter,8,Student,Readiing\n')
new_file.write('Ashley,38,Important Teacher,Learning\n')


new_file.close()

my_file = open('Family.txt', 'r')
total = 0
count=0
data = my_file.readlines()
for line in data[1:]:    #if we want just name 
    line_data = line.split(",")
    name = line_data[2]  # if we just want age
    age = float(line_data[1])
    occupation = line_data[2]
    total += age
    count += 1
    print(f"{name} is a {occupation}")
    
print(f'avg age = {total/count}')