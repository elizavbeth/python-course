numbers = [1, 2, 3, 4, 5]
energy = [2, 4, 6, 8, 10]

result = [number * 2 for number in numbers] # цикл всередині списку
high_energy = [value for value in energy if value >= 8] # цикл з умовою всередині списку
result_2 = [value * 10 for value in energy if value >= 5] # цикл з умовою для перетворення чисел на відсотки

print(result)
print(high_energy)
print(result_2)