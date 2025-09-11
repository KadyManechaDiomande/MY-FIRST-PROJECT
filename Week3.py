#Created by Kady Manecha on Sept 11

number = input("Enter a number: ")

if number > 0:
    print("It's Positive")
elif number > 1000:
    print("It's a very largely positive")
elif number > 1000000:
    print("It's a very large number")
else:
    print("It's a negative number")




    standards = int(input("Enter your standard:"))

    if standards >= 53:
        print("A")
    elif standards >= 51:
        print("A-")
    elif standards >= 49:
        print("B+")