numbers = []

for i in range(5):
    num = float(input(f"Ingresa el número real #{i + 1}: "))
    numbers.append(num)

greatest = max(numbers)
smallest = min(numbers)
total = greatest + smallest

print(f"Mayor: {greatest} | Menor: {smallest}")
print(f"La suma del mayor y el menor es: {total}")

