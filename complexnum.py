complex_list = []

with open("complex.txt", "r", encoding="utf-8") as file:
    for line in file:
        cleaned = line.strip()
        if cleaned:
            # Python usa 'j' para la parte imaginaria, así que reemplazamos 'i' si existe
            cleaned = cleaned.replace("i", "j")
            complex_list.append(complex(cleaned))

total_sum = sum(complex_list)
print("La suma de los números complejos es:", total_sum)
