'''
###################### simple calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def main():
    print("Simple CLI Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4 or 'q' to quit): ")

        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please choose a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")

if __name__ == "__main__":
    main()
'''
###############number guessing game############################
'''
import random
number = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
attempts = 0
while True:
    guess = input("Take a guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        break
  
        
 ############ list practise ######################

num=[1,2,3,4,5]
num.append(6)
num.insert(2,7)
num.remove(4)
num.pop(5)
num.sort()
num.reverse()
print(num[1:3]) 
print(num)
  
############## lambda function ######################
square = lambda x: x * x

def square(x):
    print("This is a function")
    return x * x

# Same thing with lambda

print(square(5))  # Output: 25

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, numbers)  # Filter even numbers
print(list(evens))  # Output: [2, 4, 6, 8]

### map 

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)


### reduce 
from functools import reduce

# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print("Total sum:", total)


    AND 

from functools import reduce

values = [2, 3, 4]
product = reduce(lambda x, y: x * y, values)
print("Product:", product)


################# list comprehension ######################
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]


numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x * x, numbers)  # Square each number
print(list(squared))  # Convert to list: [1, 4, 9, 16, 25]


#################tuples and dictionaries######################
# Creating the tuple
favorite_book = ("Atomic Habits", "James Clear", 2018)

# Unpacking the tuple
title, author, year = favorite_book

# Printing the statement
print(f"My favorite book is {title} by {author}, published in {year}.")

books = {
    "Atomic Habits": {"author": "James Clear", "year": 2018, "rating": 9.5},
    "Deep Work": {"author": "Cal Newport", "year": 2016, "rating": 9.0}
}
for book, details in books.items():
    print(f"{book} by {details['author']} ({details['year']}) - Rating: {details['rating']}")
'''


#################### lambda functions ######################


