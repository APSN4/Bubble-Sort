"""
by APSN4 // Реализация сортировки списка методом "пузырьком"
"""
numbers = [275, 23, 124243, 1, 555, 25, 12, 323, 2, 4535]

count = len(numbers)

for first in range(count - 1):
	for second in range(count - 1):
		if numbers[second] > numbers[second + 1]:
			numbers[second], numbers[second + 1] = numbers[second + 1], numbers[second]
			
print(numbers)