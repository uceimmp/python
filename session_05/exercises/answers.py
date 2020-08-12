#Print 10 random numbers
import random

for number in range (10):
    print(random.randint(1,10))

#Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!"
import random
guess_number = None

while guess_number != 7:
    guess_number = int(input("Enter your number: "))
print("Wow lucky number 7")


#Rewrite so that the number being guessed is a random value from 1 to 10
import random
guess = None

while guess != 7:
    guess = random.randint(1, 10)
    print(guess)
print("Wow lucky number 7")

#The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. E.g. 240cm x 80cm = 19200cm2 = 2m2
import math
width = int(input("What is the width of your rectangle:\n"))
height = int(input("What is the height of your rectangle:\n"))
rea_in_cm = width * height
area_in_m2 = math.ceil(area_in_cm/10000)
print("Your rectangle is " + str(area_in_m2) + ' metres squared.')

#Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". If they get it wrong, print "Password failure" and then ask them to enter it again. Only allow them to enter the password wrong 3 times before printing "System Locked!"
user_input = input("What is your password?\n")
correct_password = "qwerty123"
password_count = 0

while password_count < 2:
    if user_input == correct_password:
        print("You have logged in successfully")
        break
    else:
        print("Password failure")
        user_input = input("What is your password?\n")
        password_count += 1

#Add up all the numbers from 1 to 500 and print the answer
sum = 0
for i in range(1,500):
    sum += i
print(sum)

#Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. Find the index at which the user entered the number 99
num_list = []
numbers = ""
i = 0
x = 0
print("Pick 10 numbers, one of those numbers must be 99")

while i < 10:
    numbers = int(input("Pick a number:\n"))
    num_list.append(numbers)
    i += 1

while x < len(num_list):
    if num_list[x] == 99:
        print("Number 99 is at index " + str(x))
    x += 1