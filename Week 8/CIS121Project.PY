'''
#store a list of words consisting of all words with 2 or more

def string_to_list_with_vowels(word):
    words= []
    #collect a word
    built_word = ""
    vowel_count = 0
    for letter in word:
        if letter == " ":
            words.append(built_word)
            built_word = ""
        else:
            built_word += letter
    return words


my_word = "peter piper picked a peck of pickled pepprs"
print(string_to_list_with_vowels(my_word))
'''
'''''
def get_names(names):
    result = []                 # empty list to collect student names
    for tech_id in names:       # loop over dictionary KEYS (the tech IDs)
        student_name = names[tech_id]  # look up the value for this key
        result.append(student_name)    # add the name to the list
    return result
print(get_names({"01475": "Steve", "87469": "Alice", "654123": "Bob"})) 
'''

def min_grade(exams):
    min_course = ""
    min_value = 999999
    for course in exams:
        grade = exams[course]
        if grade < min_value:
            min_value = grade
            min_course = cose
    return min_course

print(min_grade({"Physics": 82, "Math": 65, "History": 75, "Biology": 95, "English": 87}))


je t'adore
je t'aime
je 

je t'aime 