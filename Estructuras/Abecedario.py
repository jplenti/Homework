Abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
Numeros_Print = []

Frase = str(input("Ingresa una frase: "))
Frase = Frase.lower()
Listar_Frase = list(Frase)

for Letra in Listar_Frase:
    if Letra in Abecedario:
        Numeros_Print.append(Abecedario.index(Letra)+1)
    else:
        print("La letra: {} ingresada no esta en el abecedario".format(Letra))

print(*Numeros_Print, sep="")