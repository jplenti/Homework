print("~ Convertir Dólares a Pesos Chilenos ~")

VALOR_DOLAR = 767.29 #Valor a dia 01-12-2020

cantidad_usd = float(input("Ingresa la cantidad de dólares a convertir: \n"))
resultado_clp = cantidad_usd * VALOR_DOLAR

print(cantidad_usd, "Dólares son:", resultado_clp, "Pesos Chilenos")
