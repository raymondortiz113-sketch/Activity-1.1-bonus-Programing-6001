sentence = input("Escribe una oración: ")
reversed_sentence = sentence[::-1]

with open("rev.txt", "w", encoding="utf-8") as file:
    file.write(reversed_sentence)

print("Oración invertida:", reversed_sentence)
print("Listo. También se guardó en 'rev.txt'.")
