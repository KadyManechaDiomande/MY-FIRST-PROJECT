#4
'''''
def get_names(my_dict):
    #Empty list to store names!
    names =[]
    #How to iterate through the dictionary
    for key in my_dict:
        #How do we acces the value with the key
        name = my_dict[key]
        #How do you put the names in a list
        names.append(Name)

    return names
name_dict = {"123"; "matt"; "lop"; "5889"}
print(get_names(name_dict))
      


#5
def find_oldest(persons):
    oldest_name = []
    max_age = -1

    #how do you iterate through the dict?
    for name in persons:
        age = persons[name]
    #how do you find the oldest age?
    if age > max_age:
         max_age = name
    #how do you get the name?
    oldest_name = name

    return oldest_name
persons = {'Emma': 71, "jack" : 52, "Olivia" : 85}

#6 
def letter_count(word):
    count_dict = {}
    
    #how do we iterate through the letters in the word?
    for letter in word:
        if letter in count_dict:
            #if letter is already there, increment value
            count_dict[letter] += 1
        else:
             #if the letter is not on dict, add letter to dict
             count_dict[letter] = 1


    return count_dict
print(letter_count("missippi"))
'''''





#class quizz

#question 1 - isogram
'''
def is_isogram(word):
    seen_letters = {}          #empty dict
    for letter in word:
        if letter in seen_letters:         #if letter was seen before it is not an isogram
            return False
        seen_letters[letter] = True             #adds/update an entry in the dictionary so that the key letter exists with a dummy value - True
    return True

print(is_isogram("algorism"))
print(is_isogram("password"))
print(is_isogram("consecutive"))
'''

# question 2 - returnign the single number that was not repeated
'''
def find_unique(numbers):
    counts = {}

    for n in numbers:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    for n in counts:                  # loop keys only
        if counts[n] == 1:
            return n
       
print(find_unique([1, 2, 2, 3, 3, 4, 4,]))
print(find_unique([7, 8, 8, 9, 9, 10, 10]))
print(find_unique([5, 6, 6, 7, 7, 8, 8, 5, 9]))
'''

# question 3 - returns the unique 2 numbers:
'''
def return_unique(numbers):
    counts = {}             #start an empty dictionary - how many times it shows up
    for n in numbers:
        counts [n] = counts.get(n, 0) + 1       #look up n's current count(or 0 if it is not there), then add 1

    uniques = []
    for n in numbers:                   #walk the list again in original order
        if counts[n] == 1:              #keep the numbers that appeared once
            uniques.append(n)
            if len(uniques) == 2:       # stop once we have two
                return uniques
    return None

print(return_unique([1, 9, 8, 8, 7, 6, 1, 6,]))           # [9, 7]
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))     # [2, 1]
print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))  # [5, 6]
'''
# question 3 - returns the unique 2 numbers: ******************************** preferred solution - if there are more than 2 unique numbers instead of just 2
'''
def return_uniques(numbers):
    count = {}
 
    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    # collect numbers that appear exactly once
    uniques = []
    for n in numbers:   # preserves input order
        if count[n] == 1:
            uniques.append(n)
    return uniques

print(return_uniques([2,2,3,4,5,4,6,5,7]))  # [3, 6, 7]
print(return_uniques([1, 9, 8, 8, 7, 6, 1, 6,]))           # [9, 7]
print(return_uniques([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))     # [2, 1]
print(return_uniques([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))  # [5, 6]
'''

#question 4 - return just the student names: *******************preferred solution
#tech id - key(must be unique) / names=values
#dicyionary was given so just extracting the values
'''
def get_names(names):
    result = []                 # empty list to collect student names
    for tech_id in names:       # loop over dictionary KEYS (the tech IDs)
        student_name = names[tech_id]  # look up the value for this key
        result.append(student_name)    # add the name to the list
    return result

# Tests
N # ['Steve', 'Alice', 'Bob']
print(get_names({"ID1": "John", "ID2": "Emma", "ID3": "Liam"}))          # ['John', 'Emma', 'Liam']
'''

#question 4 - return just the student names  -solution from lab, just change the name of variables.
'''
def get_names(names):
    result = []
    for tech_id in names:
        student_names = names[tech_id]
        result.append(student_names)
    return result

print(get_names({"01475": "Steve", "87469": "Alice", "654123": "Bob"}))  # ['Steve', 'Alice', 'Bob']
print(get_names({"ID1": "John", "ID2": "Emma", "ID3": "Liam"}))          # ['John', 'Emma', 'Liam']
print(get_names({}))
'''

# question 5  - returns the name of the oldest person
'''
def find_oldest(people):
    oldest_name = ""  #empty string
    oldest_age = -1
   
    for name in people:     #iterates keys(names)
        age = people[name]   # looks up the value (age)or the name
        if age > oldest_age:
            oldest_age = age
            oldest_name = name
    return oldest_name

# Tests
print(find_oldest({"Emma":71, "Jack":45, "Olivia":82, "Liam":39}))   # Olivia
print(find_oldest({"Sophia":50, "Mason":68, "Ava":67, "Noah":33}))   # Mason
print(find_oldest({"Ethan":25, "Lucas":30, "Mia":29}))    
'''

# question 6  - return a dcitionary with the count of each letter in the word
'''
def letter_count(word):
    count_dict = {}

    for letter in word:
        if letter in count_dict:
            count_dict[letter] += 1
       
        else:
            count_dict[letter] = 1
    return count_dict

print(letter_count("hello"))        # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(letter_count("mississippi"))  # {'m': 1, 'i': 4, 's': 4, 'p': 2}
print(letter_count("apple"))        # {'a': 1, 'p': 2, 'l': 1, 'e': 1}
'''
#question 7 - return the names of the course with the minimal grade
#exams - dict {course: grade}
# for course in exams: iterates the keys of the dict (same as "for course in exmas.keys")
# score = exmas[scores] = dictionary lookupey - value)
'''
def min_grade(exams):
 
    lowest_course = None
    lowest_grade = None

    for course in exams:
        grade = exams[course]
        if lowest_grade is None or grade < lowest_grade:
            lowest_course = course
            lowest_grade = grade
    return lowest_course

print(min_grade({"Physics":82, "Math":65, "History":75, "Biology":95, "English":87}))  # Math
print(min_grade({"Chemistry":78, "Algebra":88, "History":72, "Geography":85}))         # History
print(min_grade({"Art":90, "Music":92, "Drama":89}))                                   # Drama
'''

#question 8 - return the youngest person
'''
def find_youngest(people):
   
    youngest_name = ""      #empty string
    youngest_age = None

    for name in people:     #loop over the keys(name)
        age = people[name]  #look up the age using the key
        if youngest_age is None or age < youngest_age:
            youngest_age = age
            youngest_name = name
    return youngest_name

print(find_youngest({'Emma': 71, 'Jack': 45, 'Olivia': 82, 'Liam': 39}))     #”Liam”
print(find_youngest({ "Sophia": 50, "Mason": 68, "Ava": 67, "Noah": 33 }))   # Noah
print(find_youngest({ "Ethan": 25, "Lucas": 30, "Mia": 29 }))                # Ethan
'''

#question 9 - printing the total cost - receipt
# build the dictionary
'''
receipt = {}
receipt['Side Salad'] = 6
receipt['Chicken Parm'] = 12
receipt['Cookie'] = 3

# get the total cost
total = 0
for item in receipt:
    price = receipt[item]
    total = total + price

print(f"Total cost: ${total}")
'''

#question 10  - menu from a restaurant as key-value pairs
#build a dictionary menu
# each items on the menu
'''
menu = {}
menu['burger'] = 10
menu['fries'] = 4
menu['soda'] = 3

for name in menu:           # is the key - for key in the dictionary
    price = menu[name]      #look up the price in using the key - look up the value in the dictionary using the key
    print(f"{name} cost {price}")
'''

#question 11 - return a dictionaryon how many times each element is repeated
#empty dictionary
#go through each element
#if it was seen before add 1
'''
def count_repetitions(elements):
    counts = {}
    for x in elements:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
print(count_repetitions(["cat", "dog", "cat", "cow", "cow", "cow"]))      
# {'cat': 2, 'dog': 1, 'cow': 3}
print(count_repetitions([1, 5, 5, 5, 12, 12, 0, 0, 0, 0, 0, 0]))          
# {1: 1, 5: 3, 12: 2, 0: 6}
print(count_repetitions(["Infinity", "null", "Infinity", "null", "null"]))
# {'Infinity': 2, 'null': 3}
'''
#if answers need to be sorted highest to lowest as shown in the example:
'''
def count_repetitions_sorted(elements):
    # 1) Count occurrences
    counts = {}
    for x in elements:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    # 2) Build a new dict from highest to lowest count, no built-in sort
    result = {}

    # Keep going until we've moved all keys from counts to result
    while counts:
        # Find the key with the largest count (manual max)
        first = True
        for k in counts:                 # loop over keys
            if first:
                best_key = k
                best_count = counts[k]
                first = False
            else:
                if counts[k] > best_count:
                    best_key = k
                    best_count = counts[k]

        # Move that best_key to the result in order
        result[best_key] = best_count
        del counts[best_key]             # remove so we can find the next largest

    return result
'''

#question number 12 - returning a list of items you can afford otherwise return an empty list
'''
def items_purchase(store, wallet):
    affordable = []
    for item in store:              # item is the key (name)
        price = store[item]         # look up its price
        if price <= wallet:
            affordable.append(item)

    affordable.sort()               # alphabetical order
    return affordable

print(items_purchase({ "Water": 1, "Bread": 3, "TV": 1000 }, 300))   # ['Bread', 'Water']
print(items_purchase({ "Apple": 4, "Pan": 100, "Spoon": 2 }, 100))   # ['Apple', 'Pan', 'Spoon']
print(items_purchase({ "Phone": 999, "Laptop": 5000, "PC": 1200 }, 1)) # []
'''

#if sorting is not needed as it was not implied in the problem
'''
def items_purchase(store, wallet):
    affordable = []
    for item in store:              # item is the key (name)
        price = store[item]         # look up its price
        if price <= wallet:
            affordable.append(item)

 
    return affordable

print(items_purchase({ "Water": 1, "Bread": 3, "TV": 1000 }, 300))   # ['Bread', 'Water']
print(items_purchase({ "Apple": 4, "Pan": 100, "Spoon": 2 }, 100))   # ['Apple', 'Pan', 'Spoon']
print(items_purchase({ "Phone": 999, "Laptop": 5000, "PC": 1200 }, 1)) # []
'''

#question 13 -  return the total number of products sold
'''
def total_sales(sales):
    total = 0
    for product in sales:          # product is the key (name)
        units = sales[product]     # look up the units sold
        total = total + units
    return total

print(total_sales({"Laptop": 5, "Phone": 10, "Tablet": 3}))     # 18
print(total_sales({"Shoes": 20, "Hats": 15, "Jackets": 10}))    # 45
print(total_sales({"Book": 1, "Pen": 2, "Notebook": 1}))        # 4
'''                            

#question 14 - list of employees earning above a given salary
#remove the sort line if not needed
'''
def high_earners(employee_salaries, min_salary):
    result = []
    for name in employee_salaries:              # name is the key
        salary = employee_salaries[name]        # look up salary
        if salary > min_salary:                 # strictly above
            result.append(name)
    result.sort()                               # optional: alphabetical
    return result

print(high_earners({"Alice": 50000, "Bob": 75000, "Charlie": 100000}, 60000))  # ['Bob', 'Charlie']
print(high_earners({"David": 30000, "Emma": 45000, "Frank": 50000}, 40000))    # ['Emma', 'Frank']
print(high_earners({"George": 25000, "Hannah": 27000, "Ian": 29000}, 30000))   # []
'''

#if the result needs to be in a dictionary:
'''
def high_earners_dict(employee_salaries, min_salary):
    result = {}
    for name in employee_salaries:       # loop over keys (names)
        salary = employee_salaries[name] # look up salary
        if salary > min_salary:          # strictly above
            result[name] = salary
    return result
'''

#QUESTION 15 - returnign the total amount donated
'''
def total_donations(donations):
    total = 0
    for name in donations:        # name is the key (donor)
        amount = donations[name]  # look up the donated amount
        total = total + amount
    return total

print(total_donations({"John": 100, "Sarah": 200, "Mike": 50}))      # 350
print(total_donations({"Anna": 500, "Tom": 1000, "Jerry": 1500}))    # 3000
print(total_donations({"Chris": 25, "Alex": 30, "Morgan": 45}))
'''
#donations is a dictionary (names → amounts).
#for name in donations: iterates over the dictionary’s keys.
#donations[name] is dictionary indexing to look up the value for that key.

#question 16 - returns the total caloric value of the fruits consumed.
'''
calories = { "apple": 95, "banana": 105, "orange": 62, "grape": 3, "pear": 102 }
# given in the problem (note: 'grape' should have a colon)
def total_calories(fruits):
    total = 0
    for fruit in fruits:
        if fruit in calories:          # only add if it's a known fruit
            total = total + calories[fruit]
    return total

print(total_calories(["apple", "banana", "orange"]))                 # 262
print(total_calories(["grape", "grape", "grape", "grape", "grape"])) # 15
print(total_calories(["banana", "pear", "apple"]))                   # 302
'''

#question 17 - returns the total cost of making a recipe
'''
# given in the problem
prices = { "flour": 2.50, "sugar": 1.80, "eggs": 3.00, "milk": 2.00,
           "butter": 2.75, "vanilla": 4.50, "chocolate": 5.00 }

def total_cost(ingredients):
    total = 0.0
    for item in ingredients:
        if item in prices:          # only add known ingredients
            total = total + prices[item]
    return total        

print(total_cost(["flour", "sugar", "eggs", "butter"]))          # 10.05
print(total_cost(["milk", "vanilla", "chocolate"]))              # 11.5  -> format as 11.50 when printing
print(total_cost(["eggs", "eggs", "flour", "sugar"]))            # 10.3  -> format as 10.30 when printing

print(f"${total_cost(['milk', 'vanilla', 'chocolate']):.2f}")    # $11.50
'''

#question 18 - return the majority element
'''
def majority_element(nums):
    counts = {}
    need = (len(nums) + 1) // 2   # "at least half" threshold

    for x in nums:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

        if counts[x] >= need:     # early exit when we reach majority
            return x

print(majority_element([3,2,3]))                       # 3
print(majority_element([2,2,1,1,1,2,2]))               # 2
print(majority_element([2,2,3,2,1,2,1,4,4,1,2,2]))     # 2
'''

'''
def min_grade(exams):
    min_course = ""
    min_value = 999999
    for course in exams:
        grade = exams[course]
        if grade < min_value:
            min_value = grade
            min_course = course
    return min_course

print(min_grade({"Physics": 82, "Math": 100, "History": 75, "Biology": 95, "English": 87}))

'''


menu = {}
menu["burger"] = 10
menu["fries"] = 4
menu["soda"] = 3

for item in menu:
    print(item, menu[item])