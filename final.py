from resumen import ResumenEdades

resumen = ResumenEdades()
contador = 1  # Para numerar cada edad válida ingresada

print("👋 Ingresá edades una por una. Escribí 'fin' para terminar.\n")

while True:
    entrada = input(f"Edad {contador}: ")
    
    if entrada.lower() == "fin":
        break

    if entrada.lstrip("-").isdigit():
        edad = int(entrada)
        resumen.agregar_edad(edad)
        contador += 1  # Solo se incrementa si la entrada fue válida
    else:
        print("⚠ Edad inválida. Ingresá un número o 'fin' para terminar.")