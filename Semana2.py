from categoria import categorizar_edad

edad = int(input("Ingresa tu edad: "))

if edad.lstrip("-").isdigit():
    edad = int(edad)
    categoria = categorizar_edad(edad)
    print (f"Segun tu edad eres un {categoria}")
else:
    print("ingresaste un valor invalido")