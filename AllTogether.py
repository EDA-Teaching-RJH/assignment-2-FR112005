### Part Four -- your code goes here. 

import random

random_numbers = [random.randint(1, 100) for _ in range(10)] 
print("Original list:", random_numbers)

index = 0
while x < len(random_numbers):
    if random_numbers[x] % 2 == 0: 
        random_numbers.pop(x)
    else:
        x += 1
    print("Remaining odd numbers:", random_numbers)
