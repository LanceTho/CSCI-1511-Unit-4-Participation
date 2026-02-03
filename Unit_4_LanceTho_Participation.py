"""
Use list comprehension to create a list of 100 random numbers from 1-10
list_example = 10, 9, 8, 1, 10, 9, 4, etc.

Print out the total elements in the list
Print out the sum
Print out the average
"""
import random

random_numbers = [random.randint(1, 10) for _ in range(100)]
print(f"Here is a randomly generated list of numbers from 1-10: {random_numbers}")
print(f"Here is the total elements in the list: {len(random_numbers)}")
print(f"Here is the sum: {sum(random_numbers)}")
average: float = sum(random_numbers) / len(random_numbers)
print(f"Here is the average: {average}")