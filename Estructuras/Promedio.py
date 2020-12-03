Calificaciones = {
    "Ingles" : 70,
    "Lenguaje" : 66,
    'Historia' : 70,
    'Matematicas' : 67,
    'Fisica' : 58
}

Suma_Calificaciones = 0

for Calificacion in Calificaciones.values():
    Suma_Calificaciones += Calificacion

Promedio = Suma_Calificaciones / len(Calificaciones)

print("Tu promedio es {}".format(Promedio))

Calificacion_Mayor = max(Calificaciones.values())

print("Tu mejor materia es {a} con un promedio de: {b}".format(a=list(Calificaciones.keys())[list(Calificaciones.values()).index(Calificacion_Mayor)], b=Calificacion_Mayor))