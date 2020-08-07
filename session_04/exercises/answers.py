#Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list
Fruits = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]

#Add "Grapes" to the list and print the list
Fruits.append("Grapes")

#Change "Pears" to "Strawberries" and print the list
Fruits[2] = "Strawberries"

#Remove "Apples" from the list and print the list
del(Fruits[0])

#Print out the current length of the list
print(len(Fruits))

#Order the list alphabetically
Fruits.sort()

#Print out the list again
print(Fruits)

#Loop through the list you created in section A and print each item out
for Fruit in Fruits:
    print(Fruit)

#Print the numbers 1 to 100 (including the number 100)
for number in range(101):
    print(number)

#Print all odd numbers from 1 to 100
for number in range(101):
    if number % 2 == 1:
        print(number)

#The modern olympics started in 1896, print the years they have been held (bonus points to skip 1916, 1940, 1944)
for olympic_year in range(1896, 2021, 4):
    print(olympic_year)

#Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers
list = [10, 3, 4, 5, 1, 2, 4, 8, 9, 11]
even_count = 0
odd_count = 0

for item in list:
    if item % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("This list has " + str(even_count) + " even numbers and " + str(odd_count) + " odd numbers.")

#Create a list of five names. Write a loop that will print "Hello" plus each name in the list.

names = ["Karen", "Anna", "Aiesha", "Yogita", "Mel"]

for name in names:
    print("Hello " + name)

#Create a loop to go through each letter of the word "supercalifragilisticexpialidocious"
word = "supercalifragilisticexpialidocious"

for letter in word:
    print(letter)

#Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list

numbers = [5, 4, 3, 2, 1]
square = []

for number in numbers:
        square.append(number**2)

#Create a list with five names in. Write a for loop which appends Dr. to each name in the new list

names = ["Alex", "Felix", "Thelma", "Louise", "Fran"]
new_names = []

for name in names:
    new_names.append("Dr " + name)
    print(new_names)

#FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz"

for number in range(1, 101):
    if number % 3 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

