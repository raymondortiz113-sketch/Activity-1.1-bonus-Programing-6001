with open("numbers.txt", "r", encoding="utf-8") as file:
    numbers = [float(num) for num in file.read().split()]

numbers.sort()

with open("numbers.txt", "w", encoding="utf-8") as file:
    file.write(" ".join(str(num) for num in numbers))

print("El archivo 'numbers.txt' ha sido ordenado de forma creciente:")
print(numbers)


