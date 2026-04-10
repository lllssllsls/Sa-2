# Задание 1 вариант 12
import random

with open('f.txt', 'w') as f:
    numbers = [str(random.randint(1, 10)) for _ in range(20)]
    f.write(' '.join(numbers))

with open('f.txt', 'r') as f:
    data = f.read().split()

    unique_numbers = []
    seen = set()

    for num in data:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)

with open('g.txt', 'w') as g:
    g.write(' '.join(unique_numbers))

print("Готово! Проверьте файлы f.txt и g.txt.")