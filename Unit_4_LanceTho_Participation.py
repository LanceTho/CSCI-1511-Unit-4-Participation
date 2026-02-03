"""
Use list comprehension to create a list of random numbers from 1-10
list_example = 10, 9, 8, 1, 10, 9, 4, etc.

Print out the total elements in the list
Print out the sum
Print out the average
"""
import random

random_numbers = [random.randint(1, 10) for _ in range(100)]
print(random_numbers)