def procesar_nombres(lista_nombres):

    procesados = []

    for nombre in lista_nombres:
        limpio = nombre.strip()

        if limpio != "":
            limpio = limpio.capitalize()
            procesados.append(limpio)  
        pass

    return procesados


if __name__ == "__main__":
    nombres_sucios = ["  juan", "ALICIA", " ", "  rOberto  ", "", "   ", "cRisToBal ", "AgustinA"]
    resultado = procesar_nombres(nombres_sucios)
    print(f"Resultado final: {resultado}")