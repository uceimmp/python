# Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. Print out the string: Rectangle of width <x> and height <y> has an area of <area>
width = 5
height = 4
area = width*height

print("Rectangle of width " +  str(width) + " and height " + str(height) + " has area of " + str(area))

# Write code that prints the length of the string, 'python'
word = "python"
length = len(word)
print("The length of the word python is " + str(length))

# Print out the first and third letter of the word 'python'
word = "python"
print("The first letter of the word is " + word[0] + " the third letter of the word is " + word[2])

# Ask the user to enter their name, and print out Hello, <name>
name = str(input("Hello, what is your name? " ))
print("Hello " + name)

#Ask the user to enter their age, tell them how old they will be in 15 years time
age = input(str("How old are you now? "))
future_age = int(age) + 15
print("Your current age is " + str(age) + " your future age will be " + str(future_age))

# Combine the two input statements above
name = str(input("Hello, what is your name? " ))
age = input(str("How old are you now? "))
future_age = int(age) + 15
print("Hello, " + name + " , you are currently " + age + " years old. In 15 years time you will be " + str(future_age) )

# #Ask the user to enter their hometown, print it out in uppercase letters.
hometown = str(input("What is your hometown? "))
print(hometown.upper())

# #Ask the user to enter their favourite colour and find out the length of the colour they input
fav_colour = input(str("What is your favourite colour? "))
print("The length of your favourite colour is " + str(len(fav_colour)))

# # Ask the user to enter the weather and the month. Print out the string, It is <month> and it is <weather> today
weather = input(str("What is the weather where you are today? "))
month = input(str("What is the month today? "))

# print ("It is " + month + " and it is " + weather + " today.")

# # Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string, It is <month> and the average temperature is <average_temperature> degrees celsius.
month = input("What month is it?\n")
temp1 = int(input("What was the temperature on Monday?\n"))
temp2 = int(input("What was the temperature on Tuesday?\n"))
temp3 = int(input("What was the temperature on Wednesday?\n"))
temp4 = int(input("What was the temperature on Thursday?\n"))
temp5 = int(input("What was the temperature on Friday ?\n"))
average_temp = (temp1 + temp2 + temp3 + temp4 + temp5)/5

print("It is " + month + " and the average temperature is " + str(average_temp) + " degrees celsius.")

# # Print out the above sentence but make the month upper case
print("It is " + month.upper() + " and the average temperature is " + str(average_temp) + " degrees celsius.")

#Create a variable that holds your favourite animals and print it out. Make sure the animals are all on different lines and tabbed
animals = "My favourite animals:\n\tCats,\n\tDogs,\n\tWhales,\n\tHorses,\n\tLizards"
print(animals)

# Ask the user to enter their name as well as a number. Print out the uppercase character at that position in the string.
name = input("What is your name?\n")
number = int(input("Pick a number:\n"))

print(name[number].upper())
