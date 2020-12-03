Numbers = []
Counter = 1

while Counter <= 10:
    Number = int(input("Ingresa un numero: "))
    Numbers.append(Number)
    Counter += 1

Suma = sum(Numbers)
Promedio = Suma / len(Numbers)
Numero_Mayor = max(Numbers)
Numero_Menor = min(Numbers)

print("La suma de todos los numeros ingresados es: {}".format(Suma))
print("El promedio de todos los numeros ingresados es: {}".format(Promedio))
print("El numero mayor entre todos los numeros ingresados es: {}".format(Numero_Mayor))
print("El numero menor entre todos los numeros ingresados es: {}".format(Numero_Menor))