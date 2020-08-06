# Ask for the user's name, if they are called "Bob", print "Welcome Bob!"
user_name = str(input("What is your name? "))
if user_name == "Bob":
    print("Welcome Bob!")

# Ask for the user's name, if they are not called "Alice", print "You're not Alice!"
user_name = str(input("What is your name? "))
if user_name != "Alice":
    print("You're not Alice!")

# Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". If they get it wrong, print "Password failure"
password = input("Enter your password: ")
if password == "qwerty123":
    print("You have successfully logged in")
else:
    print("Password failure")

# Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd"
number = int(input("Enter a number: "))
if number % 2 ==0:
     print("This is an even number")
else:
     print("This is an odd number")

# Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
number_1 = int(input("What is your first number? "))
number_2 = int(input("What is your second number? "))

if number_1 + number_2 > 21:
    print("Safe")
else:
    print("Bust")

# Ask the user to enter the length and width of a shape and check if it is a square or not
length = int(input("Enter length of shape: "))
width = int(input("Enter width of shape: "))

if length == width:
    print("This shape is a square")
else:
    print("This shape is not a square")

# You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
current_salary = int(input("What is your current salary? "))
years_of_service = int(input("How many years of service have you had? "))

if years_of_service > 3:
    bonus = current_salary*0.1
    print("You will be getting " + str(bonus) + " pounds of bonus")
else:
    print("Sorry you won't be getting a bonus")

# Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
number = float(input("Enter your number ")
if number >=0:
    print(number**3)
else:
    print(number/2)

# Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", print "You're not Bob! I'm Bob", else print "You must be Charlie"
username = str(input("What is your name: "))
if username == "Alice":
    print ("Hello, Alice")
elif username == "Bob":
    print("You're not Bob! I'm Bob")
else:
    print("You must be Charlie")

# Ask the user to enter their age
# If they are younger than 11, print "You're too young to go to this school"
# If they are between 11 and 16, print "You can can come to this school"
# If they are over 16, print 'You're too old for school"
# If they are 0, print "You're not born yet!"

# age = int(input("Enter your age "))
if age < 11:
    print("You're too young to go to this school")
elif age >= 11 and age <= 16:
    print("You can can come to this school")
elif age > 16:
    print("You're too old for school")
elif age == 0:
    print("You're not born yet")
#
# Ask the user to enter the name of a month. If the user enters March/April/May: print " is in Spring", otherwise print "I don't know"
# Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February
# Ensure that when an unknown month is given it prints "I don't know"

month = str(input("Enter name of month ")
if month == "March" or month == "April" or month == "May":
    print(month + "is in Spring")
elif month == "June" or month == "July" or month == "August":
    print(month + " is in Summer")
elif month == "September" or month == "October" or month == "November":
    print(month + " is in Autumn")
elif month == "December" or month == "January" or month == "February":
    print(month + " is in Winter")
else:
    print("I don't know")

# Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers

number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))
if number_1 % 2 == 0 and number_2 % 2 == 0:
    print("This is an even number")
elif number_1 % 2 == 1 and number_2 % 2 == 1:
    print("This is an odd number")
else:
    print(number_1*number_2)

# Ask the user to input two numbers. Decide which is the number of highest value and print this out
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))

if number1 > number2:
  print(str(number1) + " has the highest value")
else:
  print(str(number2) + " has the highest value")


# You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one

current_salary = int(input("What is your current salary? "))
years_of_service = int(input("How many years of service have you had? "))

if years_of_service > 7:
    print("You will be getting " + str(current_salary*0.20) + " pounds of bonus")
elif years_of_service > 5:
    print("You will be getting " + str(current_salary*0.15) + " pounds of bonus")
elif years_of_service >=3 and years_of_service <=5:
    print("You will be getting " + str(current_salary*0.10) + " pounds of bonus")
else:
    print("You get no bonus")

# Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. If all three ages are the same, print that
name1 = input("What is your name? ")
age1 = int(input("How old are you? "))
name2 = input("What is your name? ")
age2 = int(input("How old are you? "))
name3 = input("What is your name? ")
age3 = int(input("How old are you? "))

# #Oldest
if age1 > age2 and age1 > age3:
  print(name1 + "is the oldest and is " + str(age1) + "years old.")
elif age2 > age1 and age2 > age3:
  print(name2 + "is the oldest and is " + str(age2) + "years old.")
elif age3 > age1 and age3> age2:
  print(name3 + "is the oldest and is " + str(age3) + "years old.")
else:
  ("You are all the same age")

# #Youngest
if age1 < age2 and age1 < age3:
  print(name1 + "is the youngest and is " + str(age1) + "years old.")
elif age2 < age1 and age2 < age3:
  print(name2 + "is the youngest and is " + str(age2) + "years old.")
elif age3 < age1 and age3 < age2:
  print(name3 + "is the youngest and is " + str(age3) + "years old.")
else:
  ("You are all the same age")

# A school has following rules for their grading system: a. Above 80 – A b.60 to 80 – B c.	50 to 60 – C d.	45 to 50 – D e.	25 to 45 – E f.	Below 25 - F Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lesson1 = input("Input your lesson:\n")
mark1 = int(input("Input your mark:\n"))
lesson2 = input("Input your lesson:\n")
mark2 = int(input("Input your mark:\n"))
lesson3 = input("Input your lesson:\n")
mark3 = int(input("Input your mark:\n"))

print("REPORT CARD:")

#Lesson 1
if mark1 > 80:
  print(lesson1 + " - A grade")
elif mark1 <= 80 and mark1 > 60:
  print(lesson1 + " - B grade")
elif mark1 <= 60 and mark1 > 50:
  print(lesson1 + " - C grade")
elif mark1 <= 50 and mark1 > 45:
  print(lesson1 + " - D grade")
elif mark1 <= 45 and mark1 > 25:
  print(lesson1 + " - E grade")
elif mark1 < 25:
  print(lesson1 + " - F grade")
else:
  print("Go to see your teacher")

#Lesson 2
if mark2 > 80:
  print(lesson2 + " - A grade")
elif mark2 <= 80 and mark2 > 60:
  print(lesson2 + " - B grade")
elif mark2 <= 60 and mark2 > 50:
  print(lesson2 + " - C grade")
elif mark2 <= 50 and mark2 > 45:
  print(lesson2 + " - D grade")
elif mark2 <= 45 and mark2 > 25:
  print(lesson2 + " - E grade")
elif mark2 < 25:
  print(lesson2 + " - F grade")
else:
  print("Go to see your teacher")

#Lesson 3
if mark3 > 80:
  print(lesson3 + " - A grade")
elif mark3 <= 80 and mark3 > 60:
  print(lesson3 + " - B grade")
elif mark3 <= 60 and mark3 > 50:
  print(lesson3 + " - C grade")
elif mark3 <= 50 and mark3 > 45:
  print(lesson3 + " - D grade")
elif mark3 <= 45 and mark3 > 25:
  print(lesson3 + " - E grade")
elif mark3 < 25:
  print(lesson3 + " - F grade")
else:
  print("Go to see your teacher")

