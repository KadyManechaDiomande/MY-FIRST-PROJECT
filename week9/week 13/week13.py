
import random
#option 1
rand_nums = ""
quiz_int_file = open("week 13/quizInts.txt" , "w")

for i in range(100):
   rand_num = random.randint(50,200)
   rand_num += str(rand_num)  + "\n"

quiz_int_file.write(rand_nums)
quiz_int_file. close ()
# Option 2
with open ("week 13/Quizints,txt", "w") as quiz_int_file:
   for 1 in range (100):
      rand_num = random, randint (50,200)
      rand_nuns += str(rand_num) + "In"
quiz_int_file.write(rand_nums)






#question 7
with open ("week 13/Libraryvisits.csv") as visits:
    for row in visits:
      row_items = row.split(",")
      if row_items[0] != "Date":
         total_visitor_count += int(row_items[1])
         days += 1

print(f"Average Visitor Count is {total_visitor_count/days}")
