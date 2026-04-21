numbers = {1, 2, 3, 4, 5, 6, 7, 8}

numbers_sum = 0
for num in numbers:
    if num % 2 == 0:
        numbers_sum += num

print(numbers_sum)