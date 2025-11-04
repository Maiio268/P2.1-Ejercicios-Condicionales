# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error

def pedir_n1():
    try:
        n1 = float(input("Introduce el primer numero: "))
        return n1
    except ValueError:
        print("ERROR. Introduce bien el tipo de dato.")
        return pedir_n1()

def pedir_n2():
    try:
        n2 = float(input("Introduce el segundo numero: "))
        if n2 == 0:
            print("ERROR. El dividendo no puede ser 0.")
            return pedir_n2()
        else:
            return n2
    except ValueError:
        print("ERROR. Introduce bien el tipo de dato.")
        return pedir_n2()
    
def realizar_division(n1:float, n2:float):
    division = n1 / n2
    return division

def salida(division):
    print("Resultado de la division =", division)

def main():
    # Entrada
    n1 = pedir_n1()
    n2 = pedir_n2()

    # Procesamiento
    division = realizar_division(n1, n2)

    # Salida
    salida(division)

if __name__ == "__main__":
    main()