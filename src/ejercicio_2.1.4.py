# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def entrada():
    try:
        return int(input("Introduce un numero ENTERO: "))
    except ValueError:
        print("ERROR. Hay que introducir un numero ENTERO.")
        return entrada()

def procesar_numero(n:int):
    if n % 2 == 0:
        es_par = 1
    else:
        es_par = 0
    return es_par

def salida(es_par:bool, n:int):
    if es_par == 1:
        print("El numero", n, "es par")
    else:
        print("El numero", n, "es impar")


def main():
    # Entrada
    n = entrada()

    # Procesamiento
    es_par = procesar_numero(n)

    # Salida
    salida(es_par, n)

if __name__ == "__main__":
    main()