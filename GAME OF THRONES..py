def calcular_puntos(nivel_alcanzado):
    puntos = 1000  # Puntos iniciales de Luis
    
    if nivel_alcanzado == "Pozo del Dragón":
        puntos += 19
    elif nivel_alcanzado == "Medidor de Feudos":
        puntos += 19 + 40
    elif nivel_alcanzado == "Hielo y Fuego":
        puntos += 19 + 40 + 10
    
    return puntos

nivel = input("Ingrese el nivel alcanzado (Pozo del Dragón, Medidor de Feudos, Hielo y Fuego): ")
puntos_totales = calcular_puntos(nivel)
print("Luis tiene {} puntos en total.".format(puntos_totales))
