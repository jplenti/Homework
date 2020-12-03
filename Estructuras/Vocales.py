Vocales = ["a", "e", "i", "o", "u"]
Contador = 0

Frase = str(input("Ingresa una frase: "))
Frase = Frase.lower()
Frase = list(Frase)

for Letra in Frase:
    if Letra in Vocales:
        Contador += 1

print(Contador)