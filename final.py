from resumen import ResumenEdades # type: ignore
resumen = ResumenEdades()
contador = 1 #Para enumerar las edades ingresadas
print("Ingrese edades uno por uno. Escribe 'fin' para terminar.")
while True:
    entrada = input(f"Edad{contador}:")
    if entrada.lower()== "fin":
        break
    if entrada.Istrip("-").isdigit():
        edad= int(entrada)
        resumen.agregar_edad(edad)
        contador += 1 #Solo aumenta cuando la entrada sea válida
    else:
        print("Edad errónea. Ingrese un numero o un 'fin' para terminar")
