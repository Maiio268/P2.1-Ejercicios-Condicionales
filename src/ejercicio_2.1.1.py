# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def pedir_edad():
    try:
        return int(input("Introduce tu edad: "))
    except ValueError:
        print("ERROR. Introduce bien el tipo de dato.")
        return pedir_edad()
        

def procesar_edad(edad):
    if edad >= 18:
        es_mayor = True
    else:
        es_mayor = False
    return es_mayor

def mostrar_mayor(mensaje):
    print(mensaje)

def main():
    # Entrada
    edad =  pedir_edad()

    # Procesamiento
    es_mayor = procesar_edad(edad)

    # Salida
    if es_mayor:
        mostrar_mayor("Eres mayor de edad")
    else:
        mostrar_mayor("Eres menor de edad")

if __name__ == "__main__":
    main()