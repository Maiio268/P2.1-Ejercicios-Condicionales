# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio 
# que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        return edad
    except ValueError:
        print("ERROR. Introduce un numero entero para la edad")
        return pedir_edad()

def calcular_precio(edad:int):
    if edad <= 4:
        return 0
    elif 4 < edad < 18:
        return 5
    elif edad >= 18:
        return 10

def salida(precio:int):
    print("El precio de la entrada es de:", precio, "€")

def main():
    # Entrada
    edad = pedir_edad()
    
    # Procesamiento
    precio = calcular_precio(edad)
    
    # Salida
    salida(precio)

if __name__ == "__main__":
    main()


