### Part Four -- your code goes here. 
import random

# Create a list of 10 random numbers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(10)]

# Iterate through the list with a for loop
for number in numbers[:]:
    while number % 2 == 0:
        numbers.remove(number)
        break

# Print the remaining odd numbers
print(numbers)
